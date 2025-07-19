import warnings
import os
from dotenv import load_dotenv
warnings.filterwarnings(action='ignore', category=DeprecationWarning)

# Load environment variables from .env file
load_dotenv()

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Import modules with error handling
try:
    from sms_call_utils import send_sms_twilio, make_call_twilio
    SMS_AVAILABLE = True
except ImportError:
    SMS_AVAILABLE = False
    print("Warning: SMS module not available")

try:
    from instagram_utils import post_instagram_photo
    INSTAGRAM_AVAILABLE = True
except ImportError:
    INSTAGRAM_AVAILABLE = False
    print("Warning: Instagram module not available")

try:
    from website_scraper import run_command_on_linux, run_multiple_commands_on_linux
    SSH_AVAILABLE = True
except ImportError:
    SSH_AVAILABLE = False
    print("Warning: SSH module not available")

try:
    from whatsapp_utils import send_whatsapp_message, send_whatsapp_message_twilio, send_whatsapp_instant
    WHATSAPP_AVAILABLE = True
except ImportError:
    WHATSAPP_AVAILABLE = False
    print("Warning: WhatsApp module not available")

try:
    from gmail_utils import send_gmail, send_gmail_html, send_gmail_bulk, send_gmail_template, send_gmail_newsletter
    GMAIL_AVAILABLE = True
except ImportError:
    GMAIL_AVAILABLE = False
    print("Warning: Gmail module not available")

@app.route('/api/send_sms', methods=['POST'])
def api_send_sms():
    if not SMS_AVAILABLE:
        return jsonify({'error': 'SMS service not available'}), 503
    try:
        data = request.json
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        twilio_number = os.getenv('TWILIO_PHONE_NUMBER')
        
        if not all([account_sid, auth_token, twilio_number]):
            return jsonify({'error': 'Twilio credentials not found'}), 400
        
        result = send_sms_twilio(
            account_sid, auth_token, twilio_number,
            data['to_number'], data['message']
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/make_call', methods=['POST'])
def api_make_call():
    if not SMS_AVAILABLE:
        return jsonify({'error': 'Call service not available'}), 503
    try:
        data = request.json
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        twilio_number = os.getenv('TWILIO_PHONE_NUMBER')
        
        if not all([account_sid, auth_token, twilio_number]):
            return jsonify({'error': 'Twilio credentials not found'}), 400
        
        result = make_call_twilio(
            account_sid, auth_token, twilio_number, data['to_number']
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/post_instagram', methods=['POST'])
def api_post_instagram():
    if not INSTAGRAM_AVAILABLE:
        return jsonify({'error': 'Instagram service not available'}), 503
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        if not all([username, password]):
            return jsonify({'error': 'Instagram credentials required'}), 400
        
        result = post_instagram_photo(
            username, password, data['image_path'], data['caption']
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/remote_command', methods=['POST'])
def api_remote_command():
    if not SSH_AVAILABLE:
        return jsonify({'error': 'SSH service not available'}), 503
    try:
        data = request.json
        out, err = run_command_on_linux(
            data['ip'], data['username'], data['key_path'],
            data['password'], data['command']
        )
        return jsonify({'output': out, 'error': err})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/send_whatsapp', methods=['POST'])
def api_send_whatsapp():
    if not WHATSAPP_AVAILABLE:
        return jsonify({'error': 'WhatsApp service not available'}), 503
    try:
        data = request.json
        whatsapp_number = os.getenv('WHATSAPP_NUMBER')
        
        if not whatsapp_number:
            return jsonify({'error': 'WhatsApp number not set'}), 400
        
        result = send_whatsapp_message(whatsapp_number, data['message'])
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/send_gmail', methods=['POST'])
def api_send_gmail():
    if not GMAIL_AVAILABLE:
        return jsonify({'error': 'Gmail service not available'}), 503
    try:
        data = request.json
        gmail_password = os.getenv('GMAIL_APP_PASSWORD')
        gmail_address = os.getenv('GMAIL_ADDRESS')
        
        if not all([gmail_password, gmail_address]):
            return jsonify({'error': 'Gmail credentials not found'}), 400
        
        result = send_gmail(
            gmail_address, gmail_password, data['to_email'],
            data['subject'], data['message']
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/')
def home():
    return jsonify({
        'message': 'Menu Dashboard API is running!',
        'services': {
            'sms': SMS_AVAILABLE,
            'instagram': INSTAGRAM_AVAILABLE,
            'ssh': SSH_AVAILABLE,
            'whatsapp': WHATSAPP_AVAILABLE,
            'gmail': GMAIL_AVAILABLE
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 