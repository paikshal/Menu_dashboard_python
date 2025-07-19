import warnings
import os
from dotenv import load_dotenv
warnings.filterwarnings(action='ignore', category=DeprecationWarning)

# Load environment variables from .env file
load_dotenv()

from flask import Flask, request, jsonify
from sms_call_utils import send_sms_twilio, make_call_twilio
from instagram_utils import post_instagram_photo
from website_scraper import run_command_on_linux, run_multiple_commands_on_linux
from whatsapp_utils import send_whatsapp_message, send_whatsapp_message_twilio, send_whatsapp_instant
from gmail_utils import send_gmail, send_gmail_html, send_gmail_bulk, send_gmail_template, send_gmail_newsletter

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/send_sms', methods=['POST'])
def api_send_sms():
    try:
        data = request.json
        # Use environment variables for credentials
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        twilio_number = os.getenv('TWILIO_PHONE_NUMBER')
        
        if not all([account_sid, auth_token, twilio_number]):
            return jsonify({'error': 'Twilio credentials not found in environment variables'}), 400
        
        result = send_sms_twilio(
            account_sid,
            auth_token,
            twilio_number,
            data['to_number'],
            data['message']
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/make_call', methods=['POST'])
def api_make_call():
    try:
        data = request.json
        # Use environment variables for credentials
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        twilio_number = os.getenv('TWILIO_PHONE_NUMBER')
        
        if not all([account_sid, auth_token, twilio_number]):
            return jsonify({'error': 'Twilio credentials not found in environment variables'}), 400
        
        result = make_call_twilio(
            account_sid,
            auth_token,
            twilio_number,
            data['to_number']
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/post_instagram', methods=['POST'])
def api_post_instagram():
    try:
        data = request.json
        # Use form data for Instagram credentials
        username = data.get('username')
        password = data.get('password')
        
        if not all([username, password]):
            return jsonify({'error': 'Instagram username and password are required'}), 400
        
        result = post_instagram_photo(
            username,
            password,
            data['image_path'],
            data['caption']
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/remote_command', methods=['POST'])
def api_remote_command():
    try:
        data = request.json
        out, err = run_command_on_linux(
            data['ip'],
            data['username'],
            data['key_path'],
            data['password'],
            data['command']
        )
        return jsonify({'output': out, 'error': err})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/remote_commands', methods=['POST'])
def api_remote_commands():
    try:
        data = request.json
        results = run_multiple_commands_on_linux(
            data['ip'],
            data['username'],
            data['key_path'],
            data['password'],
            data['commands']
        )
        return jsonify({'results': results})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/send_whatsapp_instant', methods=['POST'])
def api_send_whatsapp_instant():
    try:
        data = request.json
        result = send_whatsapp_instant(
            data['to_number'],
            data['message']
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/send_whatsapp', methods=['POST'])
def api_send_whatsapp():
    try:
        data = request.json
        # Use environment variables for credentials
        whatsapp_number = os.getenv('WHATSAPP_NUMBER')
        
        if not whatsapp_number:
            return jsonify({'error': 'WHATSAPP_NUMBER environment variable not set'}), 400
        
        result = send_whatsapp_message(
            whatsapp_number,
            data['message']
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/send_whatsapp_twilio', methods=['POST'])
def api_send_whatsapp_twilio():
    try:
        data = request.json
        result = send_whatsapp_message_twilio(
            data['to_number'],
            data['message']
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/send_gmail', methods=['POST'])
def api_send_gmail():
    try:
        data = request.json
        # Use environment variables for credentials
        gmail_password = os.getenv('GMAIL_APP_PASSWORD')
        gmail_address = os.getenv('GMAIL_ADDRESS')
        
        if not all([gmail_password, gmail_address]):
            return jsonify({'error': 'Gmail credentials not found in environment variables'}), 400
        
        result = send_gmail(
            gmail_address,
            gmail_password,
            data['to_email'],
            data['subject'],
            data['message'],
            data.get('is_html', False),
            data.get('attachments', None)
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/send_gmail_html', methods=['POST'])
def api_send_gmail_html():
    try:
        data = request.json
        # Use environment variables for credentials
        sender_password = os.getenv('GMAIL_APP_PASSWORD')
        if not sender_password:
            return jsonify({'error': 'GMAIL_APP_PASSWORD environment variable not set'}), 400
        gmail_address = os.getenv('GMAIL_ADDRESS')
        if not gmail_address:
            return jsonify({'error': 'GMAIL_ADDRESS environment variable not set'}), 400
        
        result = send_gmail_html(
            gmail_address,
            sender_password,
            data['to_email'],
            data['subject'],
            data['html_content'],
            data.get('attachments', None)
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/send_gmail_bulk', methods=['POST'])
def api_send_gmail_bulk():
    try:
        data = request.json
        # Use environment variables for credentials
        sender_password = os.getenv('GMAIL_APP_PASSWORD')
        if not sender_password:
            return jsonify({'error': 'GMAIL_APP_PASSWORD environment variable not set'}), 400
        gmail_address = os.getenv('GMAIL_ADDRESS')
        if not gmail_address:
            return jsonify({'error': 'GMAIL_ADDRESS environment variable not set'}), 400
        
        result = send_gmail_bulk(
            gmail_address,
            sender_password,
            data['recipients_list'],
            data['subject'],
            data['message'],
            data.get('is_html', False)
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/send_gmail_template', methods=['POST'])
def api_send_gmail_template():
    try:
        data = request.json
        # Use environment variables for credentials
        sender_password = os.getenv('GMAIL_APP_PASSWORD')
        if not sender_password:
            return jsonify({'error': 'GMAIL_APP_PASSWORD environment variable not set'}), 400
        gmail_address = os.getenv('GMAIL_ADDRESS')
        if not gmail_address:
            return jsonify({'error': 'GMAIL_ADDRESS environment variable not set'}), 400
        
        result = send_gmail_template(
            gmail_address,
            sender_password,
            data['to_email'],
            data['template_name'],
            data['template_data'],
            data.get('attachments', None)
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/send_gmail_newsletter', methods=['POST'])
def api_send_gmail_newsletter():
    try:
        data = request.json
        # Use environment variables for credentials
        sender_password = os.getenv('GMAIL_APP_PASSWORD')
        if not sender_password:
            return jsonify({'error': 'GMAIL_APP_PASSWORD environment variable not set'}), 400
        gmail_address = os.getenv('GMAIL_ADDRESS')
        if not gmail_address:
            return jsonify({'error': 'GMAIL_ADDRESS environment variable not set'}), 400
        
        result = send_gmail_newsletter(
            gmail_address,
            sender_password,
            data['subscribers_list'],
            data['newsletter_title'],
            data['newsletter_content'],
            data.get('attachments', None)
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400



@app.route('/')
def home():
    return jsonify({
        'message': 'API is running!',
        'endpoints': [
            '/api/send_sms',
            '/api/make_call', 
            '/api/post_instagram',
            '/api/remote_command',
            '/api/remote_commands',
            '/api/send_whatsapp',
            '/api/send_whatsapp_twilio',
            '/api/send_whatsapp_instant',
            '/api/send_gmail',
            '/api/send_gmail_html',
            '/api/send_gmail_bulk',
            '/api/send_gmail_template',
            '/api/send_gmail_newsletter'
        ]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 