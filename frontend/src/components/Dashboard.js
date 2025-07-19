import React from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Grid,
  Card,
  CardContent,
  CardActions,
  Button,
  Typography,
  Box
} from '@mui/material';
import {
  Email,
  Sms,
  Phone,
  Instagram,
  Computer,
  WhatsApp
} from '@mui/icons-material';

const Dashboard = () => {
  const navigate = useNavigate();

  const features = [
    {
      title: 'Send SMS',
      description: 'Send SMS messages using Twilio',
      icon: <Sms fontSize="large" />,
      path: '/sms',
      color: '#4caf50'
    },
    {
      title: 'Make Calls',
      description: 'Make phone calls using Twilio',
      icon: <Phone fontSize="large" />,
      path: '/call',
      color: '#2196f3'
    },
    {
      title: 'Instagram Post',
      description: 'Post images to Instagram',
      icon: <Instagram fontSize="large" />,
      path: '/instagram',
      color: '#e91e63'
    },
    {
      title: 'Remote Commands',
      description: 'Execute commands on remote servers',
      icon: <Computer fontSize="large" />,
      path: '/remote',
      color: '#ff9800'
    },
    {
      title: 'WhatsApp',
      description: 'Send WhatsApp messages',
      icon: <WhatsApp fontSize="large" />,
      path: '/whatsapp',
      color: '#25d366'
    },
    {
      title: 'Gmail',
      description: 'Send emails via Gmail SMTP',
      icon: <Email fontSize="large" />,
      path: '/gmail',
      color: '#ea4335'
    },

  ];

  return (
    <Box>
      <Typography variant="h4" component="h1" gutterBottom>
        Menu-Based Dashboard
      </Typography>
      <Typography variant="body1" color="text.secondary" paragraph>
        Manage your services from one menu-based interface
      </Typography>
      
      <Grid container spacing={3}>
        {features.map((feature) => (
          <Grid item xs={12} sm={6} md={4} key={feature.title}>
            <Card 
              sx={{ 
                height: '100%',
                display: 'flex',
                flexDirection: 'column',
                '&:hover': {
                  boxShadow: 6,
                  transform: 'translateY(-2px)',
                  transition: 'all 0.3s ease'
                }
              }}
            >
              <CardContent sx={{ flexGrow: 1, textAlign: 'center' }}>
                <Box sx={{ color: feature.color, mb: 2 }}>
                  {feature.icon}
                </Box>
                <Typography gutterBottom variant="h5" component="h2">
                  {feature.title}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  {feature.description}
                </Typography>
              </CardContent>
              <CardActions>
                <Button 
                  size="small" 
                  onClick={() => navigate(feature.path)}
                  sx={{ color: feature.color }}
                >
                  Open
                </Button>
              </CardActions>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
};

export default Dashboard; 