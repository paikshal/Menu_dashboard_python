"""
Send WhatsApp message using pywhatkit (system-based).
"""

import pywhatkit as kit
import datetime

def send_whatsapp_pywhatkit(phone_number: str, message: str) -> str:
    try:
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 1  # Send in 1 minute

        # Use sendwhatmsg_instantly for immediate sending
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=15, tab_close=True)
        return "WhatsApp message sent instantly using pywhatkit."
    except Exception as e:
        return f"Error sending message with pywhatkit: {str(e)}"