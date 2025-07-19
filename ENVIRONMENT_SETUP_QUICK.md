# 🔐 Quick Environment Variables Setup

## For Render.com Deployment

### 1. Gmail Setup (5 minutes)
1. Go to Gmail → Settings → Security
2. Enable 2-Factor Authentication
3. Go to App Passwords
4. Generate new app password
5. Copy the password

### 2. Twilio Setup (10 minutes)
1. Go to https://twilio.com
2. Sign up for free account
3. Go to Console → Dashboard
4. Copy Account SID and Auth Token
5. Buy a phone number ($1/month)

### 3. Add to Render.com
In your Render service → Environment tab:

```
GMAIL_APP_PASSWORD = your_gmail_app_password
TWILIO_ACCOUNT_SID = your_twilio_account_sid
TWILIO_AUTH_TOKEN = your_twilio_auth_token
TWILIO_PHONE_NUMBER = your_twilio_phone_number
WHATSAPP_NUMBER = your_whatsapp_number
```

### 4. Test Variables
After adding, your app will automatically restart and use these variables.

## Need Help?
- Gmail: https://support.google.com/accounts/answer/185833
- Twilio: https://www.twilio.com/docs/usage/secure-credentials 