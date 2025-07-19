# 🚀 Render.com Deployment Guide

## Quick Deploy Steps:

### 1. Backend Deployment
- Go to: https://render.com
- Click "New Web Service"
- Connect GitHub: `paikshal/Menu_dashboard_python`
- Configure:
  - Name: `menu-dashboard-backend`
  - Environment: `Python`
  - Build Command: `pip install -r requirements.txt`
  - Start Command: `gunicorn app:app`
  - Plan: `Free`

### 2. Environment Variables
Add these in Render dashboard:
```
GMAIL_APP_PASSWORD = your_gmail_app_password
TWILIO_ACCOUNT_SID = your_twilio_account_sid
TWILIO_AUTH_TOKEN = your_twilio_auth_token
TWILIO_PHONE_NUMBER = your_twilio_phone_number
WHATSAPP_NUMBER = your_whatsapp_number
```

### 3. Frontend Deployment
- Click "New Static Site"
- Connect same GitHub repository
- Configure:
  - Name: `menu-dashboard-frontend`
  - Build Command: `cd frontend && npm install && npm run build`
  - Publish Directory: `frontend/build`
  - Plan: `Free`

### 4. Update Frontend API URL
After backend deploys, copy the URL and update:
- Backend URL: `https://menu-dashboard-backend.onrender.com`
- Update in: `frontend/src/config.js`

## Expected URLs:
- Backend: `https://menu-dashboard-backend.onrender.com`
- Frontend: `https://menu-dashboard-frontend.onrender.com`

## Troubleshooting:
- Check Render logs for errors
- Verify environment variables
- Ensure all dependencies are in requirements.txt 