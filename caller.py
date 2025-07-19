"""
Call using Twilio or system's default calling app.
"""

import os
from dotenv import load_dotenv
from twilio.rest import Client
import webbrowser

load_dotenv()

def call_using_twilio(to_number: str) -> str:
    try:
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_PHONE_NUMBER")

        if not all([account_sid, auth_token, from_number]):
            return "Twilio credentials missing."

        client = Client(account_sid, auth_token)
        call = client.calls.create(
            to=to_number,
            from_=from_number,
            url="http://demo.twilio.com/docs/voice.xml"
        )
        return f"Call initiated. SID: {call.sid}"
    except Exception as e:
        return f"Error making call: {str(e)}"

def open_calling_app(number: str) -> str:
    try:
        webbrowser.open(f"tel:{number}")
        return f"System call UI opened for {number}"
    except Exception as e:
        return f"Error opening system dialer: {str(e)}"