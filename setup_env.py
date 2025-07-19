#!/usr/bin/env python3
"""
Environment Setup Script
This script helps you create a .env file with your credentials
"""

import os
import sys

def create_env_file():
    """Create .env file with user input"""
    
    print("🔐 Setting up your .env file for secure credential management")
    print("=" * 60)
    
    # Read existing credentials from passwords.txt if available
    existing_creds = {}
    if os.path.exists('passwords.txt'):
        try:
            with open('passwords.txt', 'r') as f:
                lines = f.readlines()
                if len(lines) >= 2:
                    existing_creds['TWILIO_ACCOUNT_SID'] = lines[0].strip()
                    existing_creds['TWILIO_AUTH_TOKEN'] = lines[1].strip()
                    print("✅ Found existing Twilio credentials in passwords.txt")
        except:
            pass
    
    # Collect credentials
    env_content = []
    env_content.append("# Environment Variables for Menu-Based Dashboard")
    env_content.append("# Copy this content to a file named .env in the project root")
    env_content.append("")
    
    # Gmail Configuration
    print("\n📧 Gmail Configuration:")
    gmail_password = input("Enter your Gmail App Password (or press Enter to skip): ").strip()
    if gmail_password:
        env_content.append(f"GMAIL_APP_PASSWORD={gmail_password}")
    
    # Twilio Configuration
    print("\n📞 Twilio Configuration:")
    account_sid = input(f"Enter Twilio Account SID (or press Enter to use existing): ").strip()
    if not account_sid and 'TWILIO_ACCOUNT_SID' in existing_creds:
        account_sid = existing_creds['TWILIO_ACCOUNT_SID']
        print(f"Using existing: {account_sid[:10]}...")
    if account_sid:
        env_content.append(f"TWILIO_ACCOUNT_SID={account_sid}")
    
    auth_token = input(f"Enter Twilio Auth Token (or press Enter to use existing): ").strip()
    if not auth_token and 'TWILIO_AUTH_TOKEN' in existing_creds:
        auth_token = existing_creds['TWILIO_AUTH_TOKEN']
        print(f"Using existing: {auth_token[:10]}...")
    if auth_token:
        env_content.append(f"TWILIO_AUTH_TOKEN={auth_token}")
    
    phone_number = input("Enter Twilio Phone Number (e.g., +1234567890): ").strip()
    if phone_number:
        env_content.append(f"TWILIO_PHONE_NUMBER={phone_number}")
    
    # WhatsApp Configuration
    print("\n💬 WhatsApp Configuration:")
    whatsapp_number = input("Enter your WhatsApp number (e.g., +1234567890): ").strip()
    if whatsapp_number:
        env_content.append(f"WHATSAPP_NUMBER={whatsapp_number}")
    
    # Instagram Configuration (optional)
    print("\n📸 Instagram Configuration (optional):")
    instagram_username = input("Enter Instagram username (or press Enter to skip): ").strip()
    if instagram_username:
        env_content.append(f"INSTAGRAM_USERNAME={instagram_username}")
        instagram_password = input("Enter Instagram password: ").strip()
        if instagram_password:
            env_content.append(f"INSTAGRAM_PASSWORD={instagram_password}")
    
    # SSH Configuration (optional)
    print("\n🔑 SSH Configuration (optional):")
    ssh_key_path = input("Enter path to SSH private key (or press Enter to skip): ").strip()
    if ssh_key_path:
        env_content.append(f"SSH_PRIVATE_KEY_PATH={ssh_key_path}")
    
    # Database Configuration (optional)
    print("\n🗄️ Database Configuration (optional):")
    db_host = input("Enter database host (default: localhost): ").strip() or "localhost"
    db_port = input("Enter database port (default: 5432): ").strip() or "5432"
    db_name = input("Enter database name (or press Enter to skip): ").strip()
    db_user = input("Enter database user (or press Enter to skip): ").strip()
    db_password = input("Enter database password (or press Enter to skip): ").strip()
    
    if db_name and db_user and db_password:
        env_content.append(f"DB_HOST={db_host}")
        env_content.append(f"DB_PORT={db_port}")
        env_content.append(f"DB_NAME={db_name}")
        env_content.append(f"DB_USER={db_user}")
        env_content.append(f"DB_PASSWORD={db_password}")
    
    # API Keys (optional)
    print("\n🔑 API Keys (optional):")
    api_key = input("Enter API key (or press Enter to skip): ").strip()
    if api_key:
        env_content.append(f"API_KEY={api_key}")
    
    secret_key = input("Enter secret key (or press Enter to skip): ").strip()
    if secret_key:
        env_content.append(f"SECRET_KEY={secret_key}")
    
    # Write to file
    env_content.append("")
    env_content.append("# End of environment variables")
    
    # Create .env file
    try:
        with open('.env', 'w') as f:
            f.write('\n'.join(env_content))
        print("\n✅ .env file created successfully!")
        print("📁 File location: .env")
        print("🔒 This file is ignored by Git for security")
        
        # Show summary
        print("\n📋 Summary of configured services:")
        if gmail_password:
            print("  ✅ Gmail")
        if account_sid and auth_token:
            print("  ✅ Twilio (SMS/Calls)")
        if whatsapp_number:
            print("  ✅ WhatsApp")
        if instagram_username:
            print("  ✅ Instagram")
        if ssh_key_path:
            print("  ✅ SSH")
        if db_name:
            print("  ✅ Database")
        if api_key or secret_key:
            print("  ✅ API Keys")
            
        print("\n🚀 You can now run your project!")
        print("   python app.py")
        print("   cd frontend && npm start")
        
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        print("\n📝 Here's the content you can manually copy to .env:")
        print("-" * 50)
        print('\n'.join(env_content))
        print("-" * 50)

def main():
    """Main function"""
    print("🔐 Menu-Based Dashboard Environment Setup")
    print("=" * 50)
    
    if os.path.exists('.env'):
        response = input("⚠️  .env file already exists. Overwrite? (y/N): ").strip().lower()
        if response != 'y':
            print("Setup cancelled.")
            return
    
    create_env_file()

if __name__ == "__main__":
    main() 