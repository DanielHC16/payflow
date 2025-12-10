"""Vercel Python Function entrypoint for PayFlow FastAPI app.

This file exposes the FastAPI `app` for Vercel Serverless Functions.
"""
from app.main import app as fastapi_app

# Vercel expects a callable named `app`
app = fastapi_app
