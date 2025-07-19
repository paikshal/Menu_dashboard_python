#!/usr/bin/env python3
"""
Create .env file for Render deployment
"""

def create_env_file():
    print("🔐 Creating .env file for Render deployment...")
    print("=" * 50)
    
    # Get user input
    print("\n📧 Gmail Configuration:")
    gmail_address = input("Enter your Gmail address: ")
    gmail_password = input("Enter your Gmail App Password: ")
    
    print("\n📞 Twilio Configuration:")
    twilio_sid = input("Enter Twilio Account SID: ")
    twilio_token = input("Enter Twilio Auth Token: ")
    twilio_number = input("Enter Twilio Phone Number: ")
    
    print("\n📱 WhatsApp Configuration:")
    whatsapp_number = input("Enter WhatsApp Number: ")
    
    # Create .env content
    env_content = f"""# Gmail Configuration
GMAIL_APP_PASSWORD={gmail_password}
GMAIL_ADDRESS={gmail_address}

# Twilio Configuration
TWILIO_ACCOUNT_SID={twilio_sid}
TWILIO_AUTH_TOKEN={twilio_token}
TWILIO_PHONE_NUMBER={twilio_number}

# WhatsApp Configuration
WHATSAPP_NUMBER={whatsapp_number}

# Application Configuration
FLASK_ENV=production
DEBUG=False
"""
    
    # Write to file
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("\n✅ .env file created successfully!")
    print("📁 File location: .env")
    print("\n🚀 Now you can:")
    print("1. Go to Render.com")
    print("2. Click 'Add from .env'")
    print("3. Select this .env file")
    print("4. Upload and deploy!")
    
    return True

if __name__ == "__main__":
    create_env_file() 