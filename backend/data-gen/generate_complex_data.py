import pandas as pd
import random
from datetime import datetime, timedelta

# --- CONFIGURATION ---
NUM_EMPLOYEES = 15
START_DATE = datetime(2025, 12, 1) # A specific week in Dec 2025
DAYS_TO_GENERATE = 7

# --- 1. GENERATE DIVERSE EMPLOYEES (Random IDs) ---
def generate_id():
    return f"EMP{random.randint(10, 999):03d}"

roles = ["Developer", "QA Engineer", "HR Specialist", "Accountant", "Intern"]
names = [
    "Juan Cruz", "Maria Santos", "Jose Reyes", "Ana Dizon", "Pedro Garcia", 
    "Liza Soberano", "Coco Martin", "Bea Alonzo", "Vice Ganda", "Catriona Gray",
    "Manny Pacquiao", "Lea Salonga", "Arnel Pineda", "Regine Velasquez", "Ben&Ben"
]

employees = []
# Ensure unique IDs
used_ids = set()

for i in range(NUM_EMPLOYEES):
    emp_id = generate_id()
    while emp_id in used_ids:
        emp_id = generate_id()
    used_ids.add(emp_id)
    
    # Random salary between 20k and 80k
    base_salary = random.randint(20, 80) * 1000 
    
    employees.append({
        "EmployeeID": emp_id,
        "Name": names[i] if i < len(names) else f"Employee {i}",
        "Role": random.choice(roles),
        "BaseSalary": base_salary,
        "Department": "Operations"
    })

df_emp = pd.DataFrame(employees)
df_emp.to_excel("employees_master.xlsx", index=False)
print(f"✅ Created employees_master.xlsx with {NUM_EMPLOYEES} staff (Random IDs).")

# --- 2. GENERATE TIME LOGS WITH "SCENARIOS" ---
logs = []

for emp in employees:
    emp_id = emp["EmployeeID"]
    
    # ASSIGN A "BEHAVIOR PROFILE" TO CREATE VARIANCE
    # 60% Normal, 10% Late, 10% OT Heavy, 10% Missing Logs, 10% Holiday Worker
    profile = random.choices(
        ['normal', 'late_riser', 'workaholic', 'forgetful', 'holiday_hero'], 
        weights=[0.6, 0.1, 0.1, 0.1, 0.1]
    )[0]

    for i in range(DAYS_TO_GENERATE):
        current_day = START_DATE + timedelta(days=i)
        is_weekend = current_day.weekday() >= 5
        
        # Skip weekends unless "workaholic"
        if is_weekend and profile != 'workaholic':
            continue

        # BASE TIMES (8:00 AM - 5:00 PM)
        clock_in_hour = 8
        clock_out_hour = 17
        
        # APPLY PROFILES
        if profile == 'late_riser':
            # Comes in between 8:30 and 9:30 (triggers Late Policy)
            clock_in_hour = 8
            clock_in_min = random.randint(30, 59)
        else:
            clock_in_min = random.randint(0, 10) # Normal variance
            
        if profile == 'workaholic':
            # Stays until 8 PM or 9 PM (Triggers OT)
            clock_out_hour = random.randint(19, 21)
            
        # GENERATE TIMESTAMPS
        clock_in = current_day.replace(hour=clock_in_hour, minute=clock_in_min, second=0)
        clock_out = current_day.replace(hour=clock_out_hour, minute=random.randint(0, 30), second=0)
        
        # ANOMALY: The "Forgetful" profile misses a punch-out on Day 3
        if profile == 'forgetful' and i == 2:
            clock_out_str = None # This will appear as NaN/Empty
        else:
            clock_out_str = clock_out.strftime("%H:%M:%S")

        logs.append({
            "EmployeeID": emp_id,
            "Date": current_day.strftime("%Y-%m-%d"),
            "ClockIn": clock_in.strftime("%H:%M:%S"),
            "ClockOut": clock_out_str,
            "Profile_Tag": profile # Helper col for you to see what happened (remove before prod)
        })

df_logs = pd.DataFrame(logs)
df_logs.to_csv("time_logs_diverse.csv", index=False)
print("✅ Created time_logs_diverse.csv with late arrivals, missing logs, and OT.")

# --- 3. GENERATE LEGACY PAYROLL (For Shadow Comparison) ---
# This creates the "Old Payroll" column data so your AI has something to mismatch against
legacy_data = []
for emp in employees:
    # "Old" payroll is usually just Base Salary / 2 (semi-monthly) approx
    # We add random noise so the AI has to calculate the EXACT difference
    old_pay = (emp["BaseSalary"] / 2) + random.randint(-500, 500)
    
    legacy_data.append({
        "EmployeeID": emp["EmployeeID"],
        "Previous_Net_Pay": round(old_pay, 2),
        "Last_Run_Date": "2025-11-30"
    })

pd.DataFrame(legacy_data).to_csv("legacy_payroll_run.csv", index=False)
print("✅ Created legacy_payroll_run.csv (Baseline for Shadow Payrolling).")

# --- 4. GENERATE POLICY ---
policy_text = """
PAYFLOW POLICY DOCUMENT (2025)
------------------------------
1. STANDARD HOURS: 08:00 to 17:00 (8 Hours work, 1 Hour Break).
2. GRACE PERIOD: Employees are allowed 15 mins grace period. 
   - Arrivals after 08:15 AM are marked "LATE".
3. OVERTIME (OT): 
   - Work beyond 17:00 is OT. 
   - Rate: 1.25x Hourly Rate.
4. HOLIDAY:
   - Dec 08 (Feast of Immaculate Conception) is a Special Non-Working Holiday.
   - Work on this day is paid 1.3x.
5. MISSING LOGS:
   - If a Clock-Out is missing, the day is marked "Incomplete" and requires manual review.
"""
with open("company_policies.txt", "w") as f:
    f.write(policy_text)
print("✅ Created company_policies.txt")