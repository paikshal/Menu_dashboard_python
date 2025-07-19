# Environment Variables Setup Guide

## ⚠️ Security Notice
This project originally contained sensitive credentials such as API keys, passwords, or tokens. For security best practices, all such sensitive information has now been removed from the source code and should be placed in a `.env` file (which is ignored in version control via `.gitignore`).

## 🚀 Quick Setup

### Step 1: Create Environment File
Copy the `env_example.txt` file to `.env`:
```bash
cp env_example.txt .env
```

### Step 2: Fill in Your Credentials
Edit the `.env` file and replace the placeholder values with your actual credentials:

```env
# Gmail Configuration
GMAIL_APP_PASSWORD=your_actual_gmail_app_password

# Twilio Configuration
TWILIO_ACCOUNT_SID=your_actual_twilio_account_sid
TWILIO_AUTH_TOKEN=your_actual_twilio_auth_token
TWILIO_PHONE_NUMBER=your_actual_twilio_phone_number

# WhatsApp Configuration
WHATSAPP_NUMBER=your_actual_whatsapp_number

# Instagram Configuration (if needed)
INSTAGRAM_USERNAME=your_actual_instagram_username
INSTAGRAM_PASSWORD=your_actual_instagram_password

# SSH Configuration (if needed)
SSH_PRIVATE_KEY_PATH=path_to_your_actual_ssh_private_key

# Database Configuration (if needed)
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_actual_database_name
DB_USER=your_actual_database_user
DB_PASSWORD=your_actual_database_password

# API Keys (if needed)
API_KEY=your_actual_api_key
SECRET_KEY=your_actual_secret_key
```

## 🔧 How to Get Your Credentials

### Gmail App Password
1. Go to your Google Account settings
2. Navigate to Security → 2-Step Verification
3. Generate an App Password for "Mail"
4. Use this password in `GMAIL_APP_PASSWORD`

### Twilio Credentials
1. Sign up at [Twilio](https://www.twilio.com/)
2. Get your Account SID and Auth Token from the dashboard
3. Get a Twilio phone number
4. Use these in `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER`

### WhatsApp Number
- Use your WhatsApp number in international format (e.g., +1234567890)

## 🛡️ Security Best Practices

1. **Never commit `.env` files** - They are already in `.gitignore`
2. **Use strong, unique passwords** for each service
3. **Rotate credentials regularly** - especially API keys
4. **Limit API permissions** - Only grant necessary access
5. **Monitor usage** - Check for unusual activity

## 🔍 Verification

After setting up your `.env` file, test the application:

1. Start the backend server:
   ```bash
   python app.py
   ```

2. Start the frontend server:
   ```bash
   cd frontend
   npm start
   ```

3. Test each feature to ensure credentials are working

## 🚨 Troubleshooting

### "Environment variable not set" Error
- Check that your `.env` file exists in the project root
- Verify the variable name matches exactly (case-sensitive)
- Restart the server after making changes

### "Invalid credentials" Error
- Double-check your API keys and passwords
- Ensure you're using the correct format (e.g., Gmail App Password vs regular password)
- Verify your accounts have the necessary permissions

### "Permission denied" Error
- Check file permissions for SSH keys
- Ensure API keys have the required scopes/permissions

## 📞 Support

If you need help with environment setup:
1. Check the service-specific documentation
2. Verify your credentials are correct
3. Contact the project maintainer

## 🔄 Updates

When updating the project:
1. Backup your `.env` file
2. Check `env_example.txt` for new variables
3. Add any new required environment variables to your `.env` file
4. Test the application after updates 