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
  Avatar,
  Chip,
  Divider
} from '@mui/material';
import { 
  ArrowBack, 
  Instagram, 
  PhotoCamera,
  Edit,
  CheckCircle,
  Error,
  Image,
  Lock
} from '@mui/icons-material';

const InstagramComponent = () => {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState('');
  const [error, setError] = useState('');
  
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    image_path: 'C:\\path\\to\\your\\image.jpg',
    caption: 'Hello from React Frontend! #python'
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
      const response = await axios.post('/api/post_instagram', formData);
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
        <Typography variant="h4" component="h1" sx={{ color: '#E4405F', fontWeight: 'bold' }}>
          Instagram Post
        </Typography>
      </Box>

      <Grid container spacing={3}>
        {/* Instagram Form */}
        <Grid item xs={12} md={6}>
          <Paper elevation={3} sx={{ p: 3, height: 'fit-content' }}>
            <Box sx={{ display: 'flex', alignItems: 'center', mb: 3 }}>
              <Avatar sx={{ bgcolor: '#E4405F', mr: 2 }}>
                <Instagram />
              </Avatar>
              <Typography variant="h6" sx={{ fontWeight: 'medium' }}>
                Instagram Post Configuration
              </Typography>
            </Box>
            
            <Typography variant="body2" color="text.secondary" sx={{ mb: 3 }}>
              Enter your Instagram credentials to post directly to your account
            </Typography>
            
            <Box component="form" onSubmit={handleSubmit} sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
              <TextField
                fullWidth
                label="Instagram Username"
                name="username"
                value={formData.username}
                onChange={handleChange}
                required
                placeholder="your_instagram_username"
                size="small"
                InputProps={{
                  startAdornment: <Instagram sx={{ mr: 1, color: 'text.secondary' }} />
                }}
              />
              
              <TextField
                fullWidth
                label="Instagram Password"
                name="password"
                type="password"
                value={formData.password}
                onChange={handleChange}
                required
                placeholder="your_instagram_password"
                size="small"
                InputProps={{
                  startAdornment: <Lock sx={{ mr: 1, color: 'text.secondary' }} />
                }}
              />
              
              <Divider sx={{ my: 1 }} />
              
              <TextField
                fullWidth
                label="Image Path"
                name="image_path"
                value={formData.image_path}
                onChange={handleChange}
                required
                placeholder="C:\\path\\to\\image.jpg"
                size="small"
                InputProps={{
                  startAdornment: <Image sx={{ mr: 1, color: 'text.secondary' }} />
                }}
              />
              
              <TextField
                fullWidth
                label="Caption"
                name="caption"
                value={formData.caption}
                onChange={handleChange}
                required
                multiline
                rows={4}
                placeholder="Write your Instagram caption here..."
                size="small"
                InputProps={{
                  startAdornment: <Edit sx={{ mr: 1, color: 'text.secondary', alignSelf: 'flex-start', mt: 1 }} />
                }}
              />
              
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mt: 1 }}>
                <Chip 
                  label={`${formData.caption.length} characters`} 
                  size="small" 
                  color={formData.caption.length > 2200 ? "warning" : "default"}
                  variant="outlined"
                />
                <Chip 
                  label="Photo Post" 
                  size="small" 
                  color="primary"
                  variant="outlined"
                  icon={<PhotoCamera />}
                />
              </Box>
              
              <Button
                type="submit"
                variant="contained"
                startIcon={loading ? <CircularProgress size={20} /> : <Instagram />}
                disabled={loading}
                sx={{ mt: 2 }}
                fullWidth
                size="large"
                style={{ backgroundColor: '#E4405F' }}
              >
                {loading ? 'Posting to Instagram...' : 'Post to Instagram'}
              </Button>
            </Box>
          </Paper>
        </Grid>

        {/* Result Panel */}
        <Grid item xs={12} md={6}>
          <Paper elevation={3} sx={{ p: 3, minHeight: 400 }}>
            <Box sx={{ display: 'flex', alignItems: 'center', mb: 3 }}>
              <Avatar sx={{ bgcolor: result ? '#4caf50' : error ? '#f44336' : '#9e9e9e', mr: 2 }}>
                {result ? <CheckCircle /> : error ? <Error /> : <Instagram />}
              </Avatar>
              <Typography variant="h6" sx={{ fontWeight: 'medium' }}>
                Instagram Status
              </Typography>
            </Box>
            
            {error && (
              <Alert severity="error" sx={{ mb: 2 }}>
                <Typography variant="body2" fontWeight="medium">
                  Instagram Post Failed
                </Typography>
                <Typography variant="body2">
                  {error}
                </Typography>
              </Alert>
            )}
            
            {result && (
              <Alert severity="success" sx={{ mb: 2 }}>
                <Typography variant="body2" fontWeight="medium">
                  Instagram Post Successful
                </Typography>
                <Typography variant="body2">
                  {result}
                </Typography>
              </Alert>
            )}
            
            {!result && !error && (
              <Card variant="outlined" sx={{ p: 3, textAlign: 'center' }}>
                <Instagram sx={{ fontSize: 48, color: '#E4405F', mb: 2 }} />
                <Typography variant="h6" color="text.secondary" gutterBottom>
                  Ready to Post on Instagram
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Enter your credentials, image path, and caption, then click "Post to Instagram" to share your content.
                </Typography>
              </Card>
            )}
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
};

export default InstagramComponent; 