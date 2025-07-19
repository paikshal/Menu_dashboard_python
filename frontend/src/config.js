const config = {
  // Development
  development: {
    API_URL: 'http://localhost:5000'
  },
  // Production - Update this with your Render backend URL
  production: {
    API_URL: 'https://menu-dashboard-backend.onrender.com'
  }
};

// Get current environment
const env = process.env.NODE_ENV || 'development';

export const API_URL = config[env].API_URL; 