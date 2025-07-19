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
  Card,
  Chip,
  Avatar
} from '@mui/material';
import { 
  ArrowBack, 
  Send, 
  Sms, 
  Phone, 
  Message,
  CheckCircle,
  Error
} from '@mui/icons-material';

const SmsComponent = () => {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState('');
  const [error, setError] = useState('');
  
  const [formData, setFormData] = useState({
    to_number: '',
    message: ''
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
      const response = await axios.post('/api/send_sms', formData);
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
        <Typography variant="h4" component="h1" sx={{ color: '#1976d2', fontWeight: 'bold' }}>
          Send SMS
        </Typography>
      </Box>

      <Grid container spacing={3}>
        {/* SMS Form */}
        <Grid item xs={12} md={6}>
          <Paper elevation={3} sx={{ p: 3, height: 'fit-content' }}>
            <Box sx={{ display: 'flex', alignItems: 'center', mb: 3 }}>
              <Avatar sx={{ bgcolor: '#1976d2', mr: 2 }}>
                <Sms />
              </Avatar>
              <Typography variant="h6" sx={{ fontWeight: 'medium' }}>
                SMS Configuration
              </Typography>
            </Box>
            
            <Box component="form" onSubmit={handleSubmit} sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
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
                placeholder="Type your message here..."
                size="small"
                InputProps={{
                  startAdornment: <Message sx={{ mr: 1, color: 'text.secondary', alignSelf: 'flex-start', mt: 1 }} />
                }}
              />
              
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mt: 1 }}>
                <Chip 
                  label={`${formData.message.length} characters`} 
                  size="small" 
                  color={formData.message.length > 160 ? "warning" : "default"}
                  variant="outlined"
                />
                {formData.message.length > 160 && (
                  <Typography variant="caption" color="warning.main">
                    Message will be split into multiple SMS
                  </Typography>
                )}
              </Box>
              
              <Button
                type="submit"
                variant="contained"
                startIcon={loading ? <CircularProgress size={20} /> : <Send />}
                disabled={loading}
                sx={{ mt: 2 }}
                fullWidth
                size="large"
              >
                {loading ? 'Sending SMS...' : 'Send SMS'}
              </Button>
            </Box>
          </Paper>
        </Grid>

        {/* Result Panel */}
        <Grid item xs={12} md={6}>
          <Paper elevation={3} sx={{ p: 3, minHeight: 400 }}>
            <Box sx={{ display: 'flex', alignItems: 'center', mb: 3 }}>
              <Avatar sx={{ bgcolor: result ? '#4caf50' : error ? '#f44336' : '#9e9e9e', mr: 2 }}>
                {result ? <CheckCircle /> : error ? <Error /> : <Message />}
              </Avatar>
              <Typography variant="h6" sx={{ fontWeight: 'medium' }}>
                SMS Status
              </Typography>
            </Box>
            
            {error && (
              <Alert severity="error" sx={{ mb: 2 }}>
                <Typography variant="body2" fontWeight="medium">
                  SMS Failed
                </Typography>
                <Typography variant="body2">
                  {error}
                </Typography>
              </Alert>
            )}
            
            {result && (
              <Alert severity="success" sx={{ mb: 2 }}>
                <Typography variant="body2" fontWeight="medium">
                  SMS Sent Successfully
                </Typography>
                <Typography variant="body2">
                  {result}
                </Typography>
              </Alert>
            )}
            
            {!result && !error && (
              <Card variant="outlined" sx={{ p: 3, textAlign: 'center' }}>
                <Sms sx={{ fontSize: 48, color: 'text.secondary', mb: 2 }} />
                <Typography variant="h6" color="text.secondary" gutterBottom>
                  Ready to Send SMS
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Fill in the phone number and message, then click "Send SMS" to deliver your message.
                </Typography>
              </Card>
            )}
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
};

export default SmsComponent; 