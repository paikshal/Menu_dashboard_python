<<<<<<< HEAD
# 🛠️ Modular Automation System using Python

This is a **terminal-based automation system** in Python that allows you to send WhatsApp messages, make phone calls, send SMS and emails, post on Instagram, and execute remote SSH commands — all from a single menu interface.

---

## 📌 Features

- ✅ WhatsApp Messaging (`pywhatkit` + `Twilio`)
- 📞 Call (via `Twilio` or system default app)
- 💬 SMS Sending
- 📧 Email Automation
- 📸 Instagram Post Uploading
- 🖥️ SSH Remote Access (supports password & public key)

---

## 🧪 Requirements

Install dependencies via:

```bash
pip install -r requirements.txt
=======
# 🚀 Menu-Based Multi-Service Dashboard

A comprehensive menu-based full-stack application that provides services for SMS, calls, Instagram posts, WhatsApp messaging, SSH remote commands, and Gmail email services.

## 🌟 Features

### 📱 Communication Services
- **SMS Service** - Send SMS using Twilio
- **Call Service** - Make phone calls using Twilio
- **WhatsApp Service** - Send WhatsApp messages (scheduled and instant)
- **Gmail Service** - Send emails with multiple options:
  - Regular emails
  - HTML emails
  - Bulk emails
  - Template emails (welcome, notification, report, custom)
  - Newsletter emails

### 📸 Social Media
- **Instagram Service** - Post photos to Instagram

### 💻 Remote Management
- **SSH Remote Commands** - Execute commands on remote Linux servers
- **Multiple Command Execution** - Run predefined command lists

### 🔐 Security Features
- **Password Protection** - Gmail credentials hidden from frontend
- **Environment Variables** - Secure credential management
- **Authentication System** - User login/logout functionality

## 🛠️ Tech Stack

### Backend
- **Python Flask** - RESTful API server
- **Twilio** - SMS and call services
- **Gmail SMTP** - Email services
- **Paramiko** - SSH connections
- **Selenium** - Instagram automation

### Frontend
- **React.js** - Modern UI framework
- **Material-UI** - Beautiful component library
- **Axios** - HTTP client for API calls
- **React Router** - Navigation

## 📦 Installation

### Prerequisites
- Python 3.8+
- Node.js 14+
- Gmail account with App Password
- Twilio account (for SMS/calls)

### Backend Setup
```bash
# Install Python dependencies
pip install flask twilio paramiko selenium python-dotenv

# Set up environment variables
# Create config/.env file with:
GMAIL_ADDRESS=your_email@gmail.com
GMAIL_APP_PASSWORD=your_app_password
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=your_twilio_number
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

## 🚀 Usage

### Start the Application
```bash
# Start Flask backend
python app.py

# Start React frontend (in another terminal)
cd frontend
npm start
```

### API Endpoints

#### SMS & Calls
- `POST /api/send_sms` - Send SMS
- `POST /api/make_call` - Make phone call

#### WhatsApp
- `POST /api/send_whatsapp` - Send scheduled WhatsApp message
- `POST /api/send_whatsapp_instant` - Send instant WhatsApp message
- `POST /api/send_whatsapp_twilio` - Send via Twilio

#### Gmail
- `POST /api/send_gmail` - Send regular email
- `POST /api/send_gmail_html` - Send HTML email
- `POST /api/send_gmail_bulk` - Send bulk emails
- `POST /api/send_gmail_template` - Send template emails
- `POST /api/send_gmail_newsletter` - Send newsletters

#### Instagram
- `POST /api/post_instagram` - Post photo to Instagram

#### SSH Commands
- `POST /api/remote_command` - Execute single command
- `POST /api/remote_commands` - Execute multiple commands

## 🔧 Configuration

### Gmail Setup
1. Enable 2-Factor Authentication
2. Generate App Password
3. Add to environment variables

### Twilio Setup
1. Create Twilio account
2. Get Account SID and Auth Token
3. Add phone number to environment variables

### SSH Setup
1. Ensure SSH service is running on target server
2. Use key-based authentication or password
3. Configure firewall settings

## 📁 Project Structure

```
menu/
├── app.py                 # Flask API server
├── gmail_utils.py         # Gmail email functions
├── whatsapp_utils.py      # WhatsApp messaging
├── sms_call_utils.py      # SMS and call functions
├── instagram_utils.py     # Instagram posting
├── website_scraper.py     # SSH remote commands
├── frontend/              # React application
│   ├── src/
│   │   ├── components/    # React components
│   │   └── App.js         # Main app component
│   └── package.json
└── README.md
```

## 🔒 Security

- Gmail app passwords are hidden from frontend
- Credentials stored in environment variables
- SSH connections use secure authentication
- API endpoints protected with error handling

## 🎯 Features in Detail

### Email Templates
- **Welcome Template** - New user onboarding
- **Notification Template** - Important alerts
- **Report Template** - Monthly metrics
- **Custom Template** - User-defined HTML

### WhatsApp Options
- **Scheduled Messages** - Send at specific times
- **Instant Messages** - Send immediately
- **Twilio Integration** - Alternative sending method

### SSH Commands
- **Single Commands** - Execute one command
- **Command Lists** - Run multiple commands
- **Real-time Output** - See command results

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

For issues and questions:
1. Check the documentation
2. Review environment setup
3. Test individual components
4. Create an issue with details

---

**Note**: This application requires proper API credentials and server access. Ensure all services are properly configured before use. 
>>>>>>> 06531d2 (Initial commit - added menu files)
