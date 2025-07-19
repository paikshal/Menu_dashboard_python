import os
import logging
from twilio.rest import Client

def send_sms_twilio(account_sid, auth_token, twilio_number, to_number, message):
    """
    Send an SMS using Twilio API.
    Args:
        account_sid (str): Twilio Account SID
        auth_token (str): Twilio Auth Token
        twilio_number (str): Twilio phone number (E.164 format)
        to_number (str): Recipient phone number (E.164 format)
        message (str): SMS message body
    Returns:
        str: Success or error message
    """
    try:
        client = Client(account_sid, auth_token)
        message_obj = client.messages.create(
            body=message,
            from_=twilio_number,
            to=to_number
        )
        return f"✅ SMS sent successfully! SID: {message_obj.sid}"
    except Exception as e:
        logging.error(f"Twilio SMS error: {e}")
        return f"Error sending SMS: {e}"

def make_call_twilio(account_sid, auth_token, twilio_number, to_number, twiml_url="http://demo.twilio.com/docs/voice.xml"):
    """
    Make a call using Twilio API.
    Args:
        account_sid (str): Twilio Account SID
        auth_token (str): Twilio Auth Token
        twilio_number (str): Twilio phone number (E.164 format)
        to_number (str): Recipient phone number (E.164 format)
        twiml_url (str): URL to TwiML instructions for the call
    Returns:
        str: Success or error message
    """
    try:
        client = Client(account_sid, auth_token)
        call = client.calls.create(
            to=to_number,
            from_=twilio_number,
            url=twiml_url
        )
        return f"✅ Call initiated successfully! SID: {call.sid}"
    except Exception as e:
        logging.error(f"Twilio call error: {e}")
        return f"Error making call: {e}" 