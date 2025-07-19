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
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Chip
} from '@mui/material';
import { ArrowBack, Email, AttachFile, Send } from '@mui/icons-material';

const GmailComponent = () => {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState('');
  const [error, setError] = useState('');
  const [emailType, setEmailType] = useState('regular'); // 'regular', 'html', 'bulk', 'template', 'newsletter'
  const [isHtml, setIsHtml] = useState(false);
  const [attachments, setAttachments] = useState([]);
  
  const [formData, setFormData] = useState({
    to_email: '',
    subject: '',
    message: '',
    html_content: '',
    recipients_list: [],
    template_name: '',
    template_data: '',
    subscribers_list: [],
    newsletter_title: '',
    newsletter_content: ''
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleFileUpload = (e) => {
    const files = Array.from(e.target.files);
    setAttachments(files.map(file => file.path || file.name));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResult('');

    try {
      let endpoint;
      let data = { ...formData };

      switch (emailType) {
        case 'html':
          endpoint = '/api/send_gmail_html';
          data.html_content = formData.html_content;
          break;
        case 'bulk':
          endpoint = '/api/send_gmail_bulk';
          data.recipients_list = formData.recipients_list.split('\n').filter(email => email.trim());
          break;
        case 'template':
          endpoint = '/api/send_gmail_template';
          data.template_name = formData.template_name;
          data.template_data = JSON.parse(formData.template_data);
          break;
        case 'newsletter':
          endpoint = '/api/send_gmail_newsletter';
          data.subscribers_list = formData.subscribers_list.split('\n').filter(email => email.trim());
          data.newsletter_title = formData.newsletter_title;
          data.newsletter_content = formData.newsletter_content;
          break;
        default:
          endpoint = '/api/send_gmail';
          data.is_html = isHtml;
          break;
      }

      // Remove password from frontend data - it will be added by backend
      delete data.sender_password;

      if (attachments.length > 0) {
        data.attachments = attachments;
      }

      // When sending the Gmail API request, always use user_id: 'prajapatipaikshal@gmail.com'
      // Example (inside the send email handler):
      // fetch('/api/send_gmail', {
      //   method: 'POST',
      //   headers: { 'Content-Type': 'application/json' },
      //   body: JSON.stringify({
      //     user_id: 'prajapatipaikshal@gmail.com',
      //     ...otherFields
      //   })
      // })
      const response = await axios.post(endpoint, data);
      setResult(response.data.result);
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  const emailTemplates = [
    {
      name: "Simple Greeting",
      subject: "Hello from API Dashboard",
      message: "Hi there!\n\nThis is a simple greeting email sent from our API Dashboard.\n\nBest regards,\nYour Team"
    },
    {
      name: "Meeting Invitation",
      subject: "Team Meeting Invitation",
      message: "Dear Team,\n\nWe would like to invite you to our weekly team meeting.\n\nDate: [Date]\nTime: [Time]\nLocation: [Location]\n\nPlease confirm your attendance.\n\nBest regards,\nTeam Lead"
    },
    {
      name: "Report Notification",
      subject: "Monthly Report Available",
      message: "Hello,\n\nThe monthly report is now available for review.\n\nPlease find the attached report and let us know if you have any questions.\n\nRegards,\nReporting Team"
    }
  ];

  const applyTemplate = (template) => {
    setFormData({
      ...formData,
      subject: template.subject,
      message: template.message
    });
  };

  return (
    <Box>
      <Box sx={{ display: 'flex', alignItems: 'center', mb: 3 }}>
        <IconButton onClick={() => navigate('/')} sx={{ mr: 2 }}>
          <ArrowBack />
        </IconButton>
        <Typography variant="h4" component="h1">
          Gmail
        </Typography>
      </Box>

      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Paper elevation={3} sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom>
              Email Configuration
            </Typography>
            
            <FormControl fullWidth sx={{ mb: 2 }}>
              <InputLabel>Email Type</InputLabel>
              <Select
                value={emailType}
                onChange={(e) => setEmailType(e.target.value)}
                label="Email Type"
              >
                <MenuItem value="regular">Regular Email</MenuItem>
                <MenuItem value="html">HTML Email</MenuItem>
                <MenuItem value="bulk">Bulk Email</MenuItem>
                <MenuItem value="template">Template Email</MenuItem>
                <MenuItem value="newsletter">Newsletter</MenuItem>
              </Select>
            </FormControl>
            
            <Box component="form" onSubmit={handleSubmit}>

              
              {emailType === 'bulk' ? (
                <TextField
                  fullWidth
                  label="Recipients (one per line)"
                  name="recipients_list"
                  value={formData.recipients_list.join('\n')}
                  onChange={(e) => setFormData({
                    ...formData,
                    recipients_list: e.target.value.split('\n')
                  })}
                  margin="normal"
                  required
                  multiline
                  rows={3}
                  placeholder="email1@example.com&#10;email2@example.com&#10;email3@example.com"
                />
              ) : emailType === 'newsletter' ? (
                <TextField
                  fullWidth
                  label="Subscribers (one per line)"
                  name="subscribers_list"
                  value={formData.subscribers_list.join('\n')}
                  onChange={(e) => setFormData({
                    ...formData,
                    subscribers_list: e.target.value.split('\n')
                  })}
                  margin="normal"
                  required
                  multiline
                  rows={3}
                  placeholder="subscriber1@example.com&#10;subscriber2@example.com&#10;subscriber3@example.com"
                />
              ) : (
                <TextField
                  fullWidth
                  label="To Email"
                  name="to_email"
                  value={formData.to_email}
                  onChange={handleChange}
                  margin="normal"
                  required
                  placeholder="recipient@example.com"
                />
              )}
              
              {emailType === 'template' && (
                <>
                  <FormControl fullWidth margin="normal">
                    <InputLabel>Template Type</InputLabel>
                    <Select
                      value={formData.template_name}
                      onChange={(e) => setFormData({
                        ...formData,
                        template_name: e.target.value
                      })}
                      label="Template Type"
                    >
                      <MenuItem value="welcome">Welcome Email</MenuItem>
                      <MenuItem value="notification">Notification</MenuItem>
                      <MenuItem value="report">Monthly Report</MenuItem>
                      <MenuItem value="custom">Custom Template</MenuItem>
                    </Select>
                  </FormControl>
                  
                  <TextField
                    fullWidth
                    label="Template Data (JSON)"
                    name="template_data"
                    value={formData.template_data}
                    onChange={handleChange}
                    margin="normal"
                    required
                    multiline
                    rows={4}
                    placeholder='{"name": "John Doe", "email": "john@example.com"}'
                    helperText="Enter template data as JSON"
                  />
                </>
              )}
              
              {emailType === 'newsletter' && (
                <>
                  <TextField
                    fullWidth
                    label="Newsletter Title"
                    name="newsletter_title"
                    value={formData.newsletter_title}
                    onChange={handleChange}
                    margin="normal"
                    required
                  />
                  
                  <TextField
                    fullWidth
                    label="Newsletter Content (HTML)"
                    name="newsletter_content"
                    value={formData.newsletter_content}
                    onChange={handleChange}
                    margin="normal"
                    required
                    multiline
                    rows={6}
                    placeholder="<h2>Newsletter Content</h2><p>Your content here...</p>"
                  />
                </>
              )}
              
              {emailType !== 'template' && emailType !== 'newsletter' && (
                <TextField
                  fullWidth
                  label="Subject"
                  name="subject"
                  value={formData.subject}
                  onChange={handleChange}
                  margin="normal"
                  required
                />
              )}
              
              {emailType === 'html' ? (
                <TextField
                  fullWidth
                  label="HTML Content"
                  name="html_content"
                  value={formData.html_content}
                  onChange={handleChange}
                  margin="normal"
                  required
                  multiline
                  rows={6}
                  placeholder="<h1>Hello!</h1><p>HTML content here...</p>"
                />
              ) : (
                <TextField
                  fullWidth
                  label="Message"
                  name="message"
                  value={formData.message}
                  onChange={handleChange}
                  margin="normal"
                  required
                  multiline
                  rows={6}
                />
              )}
              
              {emailType === 'regular' && (
                <FormControlLabel
                  control={
                    <Switch
                      checked={isHtml}
                      onChange={(e) => setIsHtml(e.target.checked)}
                    />
                  }
                  label="Send as HTML"
                  sx={{ mb: 2 }}
                />
              )}
              
              <Button
                variant="outlined"
                component="label"
                startIcon={<AttachFile />}
                sx={{ mb: 2 }}
                fullWidth
              >
                Add Attachments
                <input
                  type="file"
                  multiple
                  hidden
                  onChange={handleFileUpload}
                />
              </Button>
              
              {attachments.length > 0 && (
                <Box sx={{ mb: 2 }}>
                  <Typography variant="subtitle2" gutterBottom>
                    Attachments:
                  </Typography>
                  <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1 }}>
                    {attachments.map((file, index) => (
                      <Chip
                        key={index}
                        label={file}
                        onDelete={() => setAttachments(attachments.filter((_, i) => i !== index))}
                        size="small"
                      />
                    ))}
                  </Box>
                </Box>
              )}
              
              <Button
                type="submit"
                variant="contained"
                startIcon={loading ? <CircularProgress size={20} /> : <Send />}
                disabled={loading}
                sx={{ mt: 2 }}
                fullWidth
              >
                {loading ? 'Sending...' : 'Send Email'}
              </Button>
            </Box>
          </Paper>
        </Grid>

        <Grid item xs={12} md={6}>
          <Paper elevation={3} sx={{ p: 3, minHeight: '400px' }}>
            <Typography variant="h6" gutterBottom>
              Result
            </Typography>
            
            {error && (
              <Alert severity="error" sx={{ mb: 2 }}>
                {error}
              </Alert>
            )}
            
            {result && (
              <Alert severity="info" sx={{ mb: 2 }}>
                {result}
              </Alert>
            )}
            
            {!result && !error && (
              <Typography variant="body2" color="text.secondary">
                Fill in the form and click "Send Email" to see results here.
              </Typography>
            )}
          </Paper>
        </Grid>

        <Grid item xs={12}>
          <Paper elevation={3} sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom>
              Email Templates
            </Typography>
            <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
              Click on any template to apply it:
            </Typography>
            
            <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 2 }}>
              {emailTemplates.map((template, index) => (
                <Button
                  key={index}
                  variant="outlined"
                  onClick={() => applyTemplate(template)}
                  startIcon={<Email />}
                >
                  {template.name}
                </Button>
              ))}
            </Box>
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
};

export default GmailComponent; 