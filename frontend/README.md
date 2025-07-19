# API Dashboard Frontend

A modern React frontend for managing your API services including SMS, calls, Instagram posting, remote commands, and WhatsApp messaging.

## Features

- 🔐 **Authentication System** - Login/logout with session persistence
- 📱 **SMS Management** - Send SMS via Twilio
- 📞 **Call Management** - Make calls via Twilio
- 📸 **Instagram Integration** - Post images to Instagram
- 💻 **Remote Commands** - Execute commands on remote servers via SSH
- 💬 **WhatsApp Messaging** - Send WhatsApp messages via pywhatkit or Twilio
- 🎨 **Modern UI** - Built with Material-UI for a beautiful, responsive interface
- 🔄 **Real-time Results** - Live feedback for all API operations

## Prerequisites

- Node.js (v14 or higher)
- npm or yarn
- Backend Flask API running on `localhost:5000`

## Installation

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```

4. **Open your browser:**
   Navigate to `http://localhost:3000`

## Usage

### Login
- **Username:** `admin`
- **Password:** `password`

### Features

#### SMS
- Configure Twilio credentials
- Send SMS messages to any verified number
- Real-time status updates

#### Calls
- Make phone calls using Twilio
- Configure call parameters
- View call status

#### Instagram
- Post images to Instagram
- Add captions and hashtags
- Configure Instagram credentials

#### Remote Commands
- Execute single or multiple commands on remote servers
- Support for both password and key-based SSH authentication
- Real-time command output display

#### WhatsApp
- Send WhatsApp messages via pywhatkit or Twilio
- Toggle between different sending methods
- Message status tracking

## API Endpoints

The frontend communicates with these backend endpoints:

- `POST /api/send_sms` - Send SMS
- `POST /api/make_call` - Make calls
- `POST /api/post_instagram` - Post to Instagram
- `POST /api/remote_command` - Execute single command
- `POST /api/remote_commands` - Execute multiple commands
- `POST /api/send_whatsapp` - Send WhatsApp (pywhatkit)
- `POST /api/send_whatsapp_twilio` - Send WhatsApp (Twilio)

## Security Features

- **Protected Routes** - All features require authentication
- **Session Persistence** - Login state saved in localStorage
- **Input Validation** - Form validation on all inputs
- **Error Handling** - Comprehensive error handling and user feedback

## Customization

### Styling
- Uses Material-UI theme system
- Customizable colors and components
- Responsive design for all screen sizes

### Authentication
- Modify `Login.js` to integrate with your authentication system
- Update `App.js` for custom auth logic

### API Configuration
- Update API endpoints in individual components
- Modify request/response handling as needed

## Troubleshooting

### Common Issues

1. **Backend Connection Error**
   - Ensure Flask backend is running on `localhost:5000`
   - Check CORS settings in backend

2. **Authentication Issues**
   - Clear browser localStorage
   - Check login credentials

3. **API Errors**
   - Verify API credentials (Twilio, Instagram, etc.)
   - Check network connectivity

## Development

### Project Structure
```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── Login.js
│   │   ├── Dashboard.js
│   │   ├── SmsComponent.js
│   │   ├── CallComponent.js
│   │   ├── InstagramComponent.js
│   │   ├── RemoteCommandComponent.js
│   │   └── WhatsAppComponent.js
│   ├── App.js
│   └── index.js
├── package.json
└── README.md
```

### Adding New Features
1. Create new component in `src/components/`
2. Add route in `App.js`
3. Update dashboard navigation
4. Add corresponding backend endpoint

## License

This project is for educational purposes. Please ensure you have proper licenses for all third-party services (Twilio, Instagram, etc.). 