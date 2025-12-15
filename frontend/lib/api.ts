/**
 * Get the API base URL based on environment
 * - Production: Use NEXT_PUBLIC_API_URL environment variable or default to backend Vercel URL
 * - Development: Use window.location.hostname with port 8000 for local development
 */
export function getApiBaseUrl(): string {
  // In production, use environment variable
  if (process.env.NEXT_PUBLIC_API_URL) {
    return process.env.NEXT_PUBLIC_API_URL;
  }
  
  // In browser (development), use current hostname with port 8000
  if (typeof window !== 'undefined') {
    const hostname = window.location.hostname;
    // If on Vercel, use the backend URL from env
    if (hostname.includes('vercel.app')) {
      return process.env.NEXT_PUBLIC_API_URL || 'https://payflow-backend.vercel.app';
    }
    return `http://${hostname}:8000`;
  }
  
  return 'http://localhost:8000';
}
