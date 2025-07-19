"""
Send WhatsApp message using Twilio API.
"""

import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

def send_whatsapp_twilio(to_number: str, message: str) -> str:
    try:
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_whatsapp_number = "whatsapp:" + os.getenv("TWILIO_PHONE_NUMBER")
        to_whatsapp_number = "whatsapp:" + to_number

        if not all([account_sid, auth_token, from_whatsapp_number]):
            return "Twilio credentials not set properly."

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_=from_whatsapp_number,
            to=to_whatsapp_number
        )
        return f"WhatsApp message sent. SID: {message.sid}"
    except Exception as e:
        return f"Error sending WhatsApp message: {str(e)}"