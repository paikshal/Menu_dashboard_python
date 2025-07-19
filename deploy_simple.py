#!/usr/bin/env python3
"""
Simple Deployment Script for Render.com
This script will guide you through the deployment process
"""

import webbrowser
import os
import sys

def main():
    print("🚀 Welcome to Simple Render Deployment!")
    print("=" * 50)
    
    print("\n📋 What you need to do:")
    print("1. Click the link below to go to Render.com")
    print("2. Sign up with your GitHub account")
    print("3. Click 'New Web Service'")
    print("4. Select your repository: paikshal/Menu_dashboard_python")
    print("5. Everything else will be auto-configured!")
    
    print("\n🔗 Opening Render.com...")
    
    # Open Render.com
    webbrowser.open("https://render.com")
    
    print("\n✅ Render.com opened in your browser!")
    print("\n📝 Next Steps:")
    print("1. Sign up with GitHub")
    print("2. Click 'New Web Service'")
    print("3. Connect repository: paikshal/Menu_dashboard_python")
    print("4. Name: menu-dashboard-backend")
    print("5. Environment: Python")
    print("6. Build Command: pip install -r requirements.txt")
    print("7. Start Command: gunicorn app:app")
    print("8. Plan: Free")
    print("9. Click 'Create Web Service'")
    
    print("\n🔐 Environment Variables (add these later):")
    print("- GMAIL_APP_PASSWORD")
    print("- TWILIO_ACCOUNT_SID") 
    print("- TWILIO_AUTH_TOKEN")
    print("- TWILIO_PHONE_NUMBER")
    print("- WHATSAPP_NUMBER")
    
    print("\n🎉 That's it! Your app will be deployed automatically!")
    
    input("\nPress Enter when you're ready to continue...")

if __name__ == "__main__":
    main() 