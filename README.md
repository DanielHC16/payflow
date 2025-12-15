# Home Credit PayFlow

**Top 10 Finalists - Home Credit x KadaKareer AI Hackathon**

An innovative B2B2C payroll platform featuring AI-powered migration and Employee Wage Access (EWA), designed to revolutionize payroll management and financial wellness for businesses and their employees.

## Team Wagwan

- **Daniel Camacho** - Pamantasan ng Lungsod ng Maynila
- **John Yamul** - Bulacan State University
- **Simonee Mariquit** - University of the Philippines Diliman
- **Julianne Reyes** - Mapua University

## Features

- **AI-Powered Migration Studio** - Seamlessly migrate payroll data with intelligent mapping and validation
- **Employee Wage Access (EWA)** - Provide employees early access to earned wages
- **Real-time Analytics** - AI-driven insights for payroll optimization
- **Progressive Web App** - Mobile-first employee experience
- **Secure & Compliant** - Built with data security and privacy in mind

## Quick Start (Local Development)

### Prerequisites
- Node.js 18+
- Python 3.10+
- npm or yarn

### Installation

```bash
# Install all dependencies
npm install
npm run install:all
```

### Running the Application

```bash
# Start both backend and frontend
npm run dev
```

This will start:
- **Backend API** at `http://0.0.0.0:8000`
- **Frontend** at `http://localhost:3000`

### Demo

**Desktop (Employer View):**
- Open `http://localhost:3000` in your browser
- Navigate through tabs: Dashboard, Migration Studio, Employee Data, AI Insights, ADA Strategy

**Mobile (Employee View):**
- Scan the QR code from the "Scan for Mobile" button, or
- Visit `http://<your-lan-ip>:3000` on your mobile device
- Access earnings and explore the EWA cashout flow

## Tech Stack

- **Frontend:** Next.js 16, TypeScript, Tailwind CSS, PWA
- **Backend:** FastAPI, Python, Pandas
- **AI/ML:** OpenAI GPT-4, Intelligent Data Processing
- **Deployment:** Vercel (Serverless Functions)
- **Mobile:** Progressive Web App (PWA)

---

Built by Team Wagwan for the Home Credit x KadaKareer AI Hackathon