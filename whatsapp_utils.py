import pywhatkit as kit
import datetime
import os
import logging
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv(dotenv_path=os.path.join('config', '.env'))

def send_whatsapp_instant(to_number: str, message: str) -> str:
    """
    Send a WhatsApp message instantly using pywhatkit. Returns status string.
    """
    try:
        print(f"Attempting to send INSTANT WhatsApp message to {to_number}")
        print(f"Message: {message}")
        
        # Try multiple approaches for better reliability
        try:
            # First try: instant sending with proper timing
            kit.sendwhatmsg_instantly(to_number, message, wait_time=20, tab_close=True, close_time=5)
            status = "Message sent INSTANTLY using pywhatkit!"
            print("Message sent instantly!")
        except Exception as instant_error:
            print(f"Instant method failed: {instant_error}")
            
            # Fallback: schedule for 1 minute later
            now = datetime.datetime.now()
            minute = now.minute + 1
            hour = now.hour
            if minute >= 60:
                minute = 0
                hour = (hour + 1) % 24
                
            kit.sendwhatmsg(to_number, message, hour, minute, wait_time=20, tab_close=True, close_time=5)
            status = "Message scheduled and sent using pywhatkit!"
            print("Message sent via fallback method!")
            
    except Exception as e:
        status = f"Error sending instant message: {str(e)}"
        print(f"Error occurred: {e}")
    return status

def send_whatsapp_message(to_number: str, message: str) -> str:
    """
    Send a WhatsApp message using pywhatkit. Returns status string.
    """
    try:
        print(f"Attempting to send WhatsApp message to {to_number}")
        print(f"Message: {message}")
        
        now = datetime.datetime.now()
        # Schedule for current minute + 1 to ensure it's in the future
        minute = now.minute + 1
        hour = now.hour
        if minute >= 60:
            minute = 0
            hour = (hour + 1) % 24
            
        print(f"Scheduling message for {hour}:{minute:02d}")
        
        # Use proper wait time for reliable delivery
        kit.sendwhatmsg(to_number, message, hour, minute, wait_time=15, tab_close=True, close_time=3)
        status = "Message sent using pywhatkit!"
        print("Message sent successfully!")
    except Exception as e:
        status = f"Error sending message: {str(e)}"
        print(f"Error occurred: {e}")
    return status

def send_whatsapp_message_twilio(to_number: str, message: str) -> str:
    """
    Send a WhatsApp message using Twilio API. Returns status string.
    """
    try:
        print(f"Attempting to send Twilio WhatsApp message to {to_number}")
        print(f"Message: {message}")
        
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
        if not all([account_sid, auth_token, twilio_number]):
            return 'Twilio credentials not set properly in environment variables.'
        from_whatsapp_number = 'whatsapp:' + twilio_number
        to_whatsapp_number = 'whatsapp:' + to_number
        client = Client(account_sid, auth_token)
        message_obj = client.messages.create(
            body=message,
            from_=from_whatsapp_number,
            to=to_whatsapp_number
        )
        status = f'WhatsApp message sent via Twilio. SID: {message_obj.sid}'
        print(f"Twilio message sent successfully! SID: {message_obj.sid}")
    except Exception as e:
        status = f'Error sending WhatsApp message via Twilio: {str(e)}'
        print(f"Twilio error: {e}")
    return status

def save_whatsapp_log(to_number: str, message: str, status: str):
    """
    Save WhatsApp message log to whatsapp_log.txt
    """
    with open("whatsapp_log.txt", "a", encoding="utf-8") as f:
        log_entry = f"{datetime.datetime.now()} | To: {to_number} | Message: {message} | Status: {status}\n"
        f.write(log_entry) 