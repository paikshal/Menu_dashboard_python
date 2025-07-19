import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import {
  Box,
  Paper,
  TextField,
  Button,
  Typography,
  Alert,
  Grid,
  CircularProgress,
  IconButton,
  FormControlLabel,
  Switch,
  Card,
  Avatar,
  Chip,
  Divider
} from '@mui/material';
import { 
  ArrowBack, 
  WhatsApp, 
  Phone, 
  Message,
  Speed,
  CheckCircle,
  Error,
  Bolt,
  Send
} from '@mui/icons-material';

const WhatsAppComponent = () => {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState('');
  const [error, setError] = useState('');
  const [useTwilio, setUseTwilio] = useState(false);
  const [useInstant, setUseInstant] = useState(false);
  
  const [formData, setFormData] = useState({
    to_number: '+919876543210',
    message: 'Hello from React WhatsApp!'
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResult('');

    try {
      let endpoint;
      if (useInstant) {
        endpoint = '/api/send_whatsapp_instant';
      } else if (useTwilio) {
        endpoint = '/api/send_whatsapp_twilio';
      } else {
        endpoint = '/api/send_whatsapp';
      }
      
      const response = await axios.post(endpoint, formData);
      setResult(response.data.result);
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box sx={{ p: 3, maxWidth: 1200, margin: '0 auto' }}>
      {/* Header */}
      <Box sx={{ display: 'flex', alignItems: 'center', mb: 3 }}>
        <IconButton onClick={() => navigate('/')} sx={{ mr: 2 }}>
          <ArrowBack />
        </IconButton>
        <Typography variant="h4" component="h1" sx={{ color: '#25D366', fontWeight: 'bold' }}>
          WhatsApp
        </Typography>
      </Box>

      <Grid container spacing={3}>
        {/* WhatsApp Form */}
        <Grid item xs={12} md={6}>
          <Paper elevation={3} sx={{ p: 3, height: 'fit-content' }}>
            <Box sx={{ display: 'flex', alignItems: 'center', mb: 3 }}>
              <Avatar sx={{ bgcolor: '#25D366', mr: 2 }}>
                <WhatsApp />
              </Avatar>
              <Typography variant="h6" sx={{ fontWeight: 'medium' }}>
                WhatsApp Configuration
              </Typography>
            </Box>
            
            <Box component="form" onSubmit={handleSubmit} sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
              {/* Mode Switches */}
              <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1, mb: 2 }}>
                <FormControlLabel
                  control={
                    <Switch
                      checked={useTwilio}
                      onChange={(e) => setUseTwilio(e.target.checked)}
                      color="primary"
                    />
                  }
                  label={
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                      <Typography variant="body2">Use Twilio API</Typography>
                      <Chip label="Premium" size="small" color="primary" variant="outlined" />
                    </Box>
                  }
                />
                
                <FormControlLabel
                  control={
                    <Switch
                      checked={useInstant}
                      onChange={(e) => setUseInstant(e.target.checked)}
                      color="success"
                    />
                  }
                  label={
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                      <Typography variant="body2">Instant Delivery</Typography>
                      <Chip label="Fast" size="small" color="success" variant="outlined" icon={<Bolt />} />
                    </Box>
                  }
                />
              </Box>

              <Divider sx={{ my: 1 }} />

              <TextField
                fullWidth
                label="Phone Number"
                name="to_number"
                value={formData.to_number}
                onChange={handleChange}
                required
                placeholder="+919876543210"
                size="small"
                InputProps={{
                  startAdornment: <Phone sx={{ mr: 1, color: 'text.secondary' }} />
                }}
              />
              
              <TextField
                fullWidth
                label="Message"
                name="message"
                value={formData.message}
                onChange={handleChange}
                required
                multiline
                rows={4}
                placeholder="Type your WhatsApp message here..."
                size="small"
                InputProps={{
                  startAdornment: <Message sx={{ mr: 1, color: 'text.secondary', alignSelf: 'flex-start', mt: 1 }} />
                }}
              />
              
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mt: 1 }}>
                <Chip 
                  label={`${formData.message.length} characters`} 
                  size="small" 
                  color={formData.message.length > 1000 ? "warning" : "default"}
                  variant="outlined"
                />
                <Chip 
                  label={useInstant ? "Instant" : "Scheduled"} 
                  size="small" 
                  color={useInstant ? "success" : "default"}
                  variant="outlined"
                  icon={useInstant ? <Speed /> : <Send />}
                />
              </Box>
              
              {useInstant && (
                <Typography variant="caption" color="info.main" sx={{ fontStyle: 'italic' }}>
                  💡 Tip: Make sure WhatsApp Web is open and you're logged in for instant delivery
                </Typography>
              )}
              
              <Button
                type="submit"
                variant="contained"
                startIcon={loading ? <CircularProgress size={20} /> : <WhatsApp />}
                disabled={loading}
                sx={{ mt: 2 }}
                fullWidth
                size="large"
                style={{ backgroundColor: '#25D366' }}
              >
                {loading ? 'Sending WhatsApp...' : 'Send WhatsApp'}
              </Button>
            </Box>
          </Paper>
        </Grid>

        {/* Result Panel */}
        <Grid item xs={12} md={6}>
          <Paper elevation={3} sx={{ p: 3, minHeight: 400 }}>
            <Box sx={{ display: 'flex', alignItems: 'center', mb: 3 }}>
              <Avatar sx={{ bgcolor: result ? '#4caf50' : error ? '#f44336' : '#9e9e9e', mr: 2 }}>
                {result ? <CheckCircle /> : error ? <Error /> : <WhatsApp />}
              </Avatar>
              <Typography variant="h6" sx={{ fontWeight: 'medium' }}>
                WhatsApp Status
              </Typography>
            </Box>
            
            {error && (
              <Alert severity="error" sx={{ mb: 2 }}>
                <Typography variant="body2" fontWeight="medium">
                  WhatsApp Failed
                </Typography>
                <Typography variant="body2">
                  {error}
                </Typography>
              </Alert>
            )}
            
            {result && (
              <Alert severity="success" sx={{ mb: 2 }}>
                <Typography variant="body2" fontWeight="medium">
                  WhatsApp Sent Successfully
                </Typography>
                <Typography variant="body2">
                  {result}
                </Typography>
              </Alert>
            )}
            
            {!result && !error && (
              <Card variant="outlined" sx={{ p: 3, textAlign: 'center' }}>
                <WhatsApp sx={{ fontSize: 48, color: '#25D366', mb: 2 }} />
                <Typography variant="h6" color="text.secondary" gutterBottom>
                  Ready to Send WhatsApp
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Enter the phone number and message, then click "Send WhatsApp" to deliver your message.
                </Typography>
              </Card>
            )}
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
};

export default WhatsAppComponent; 