import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
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
  List,
  ListItem,
  ListItemText,
  ListItemIcon,
  Chip,
  Divider,
  Accordion,
  AccordionSummary,
  AccordionDetails,
  FormControl,
  InputLabel,
  Select,
  MenuItem
} from '@mui/material';
import {
  ArrowBack,
  Computer,
  Terminal,
  Code,
  Storage,
  NetworkCheck,
  Security,
  Build,
  Monitor,
  Folder,
  FileCopy,
  Settings,
  PlayArrow,
  ExpandMore,
  List as ListIcon,
  Code as CodeIcon
} from '@mui/icons-material';

// Categorized inbuilt commands with section headers
const INBUILT_COMMANDS = [
  { label: 'Basic File & Directory Commands', commands: [
    'ls', 'pwd', 'cd', 'mkdir', 'rmdir', 'touch', 'cp', 'mv', 'rm', 'tree', 'find', 'locate', 'stat', 'file', 'basename', 'dirname', 'du', 'df', 'lsblk', 'mount', 'umount'
  ]},
  { label: 'File Content Viewing', commands: [
    'cat', 'more', 'less', 'head', 'tail', 'tac', 'nl', 'strings', 'wc', 'cut', 'awk', 'sed', 'grep', 'diff', 'cmp'
  ]},
  { label: 'File Permissions & Ownership', commands: [
    'chmod', 'chown', 'chgrp', 'umask', 'stat', 'getfacl', 'setfacl'
  ]},
  { label: 'Archiving & Compression', commands: [
    'tar', 'zip', 'unzip', 'gzip', 'gunzip', 'bzip2', 'bunzip2', 'xz', 'unxz', 'rar', 'unrar'
  ]},
  { label: 'Process Management', commands: [
    'ps', 'top', 'htop', 'kill', 'killall', 'nice', 'renice', 'bg', 'fg', 'jobs', '&', 'nohup', 'pgrep'
  ]},
  { label: 'User Management', commands: [
    'whoami', 'id', 'who', 'users', 'adduser', 'useradd', 'deluser', 'userdel', 'passwd', 'su', 'sudo', 'groupadd', 'groupdel', 'groups', 'gpasswd'
  ]},
  { label: 'Networking', commands: [
    'ifconfig', 'ip a', 'ping', 'traceroute', 'netstat', 'ss', 'curl', 'wget', 'scp', 'rsync', 'dig', 'nslookup', 'hostname', 'nmap', 'telnet', 'ssh', 'ftp', 'arp'
  ]},
  { label: 'Package Management (Ubuntu/Debian)', commands: [
    'apt update', 'apt upgrade', 'apt install <pkg>', 'apt remove <pkg>', 'apt purge <pkg>', 'apt search <pkg>', 'apt show <pkg>', 'dpkg -i <pkg.deb>', 'dpkg -r <pkg>', 'dpkg -l'
  ]},
  { label: 'System Monitoring', commands: [
    'uptime', 'free -h', 'vmstat', 'iostat', 'sar', 'dmesg', 'watch'
  ]},
  { label: 'Disk & Filesystem', commands: [
    'fdisk', 'parted', 'mkfs', 'fsck', 'mount', 'umount', 'blkid', 'lsblk', 'df -h', 'du -sh *'
  ]},
  { label: 'Text Editors', commands: [
    'nano', 'vim', 'vi', 'emacs', 'gedit', 'code'
  ]},
  { label: 'System Info', commands: [
    'uname -a', 'lsb_release -a', 'cat /etc/os-release', 'top', 'uptime', 'hostnamectl', 'lscpu', 'lsblk', 'lsmem', 'lspci', 'lsusb', 'dmidecode'
  ]},
  { label: 'Scripting & Automation', commands: [
    'bash <script.sh>', './script.sh', 'crontab -e', 'at', 'watch', 'alias', 'export VAR=value', 'env', 'source file.sh'
  ]},
  { label: 'Fun Commands', commands: [
    'cowsay "Hello"', 'fortune', 'sl', 'cmatrix', 'neofetch', 'figlet "Linux"'
  ]}
];

function RemoteCommandComponent() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [form, setForm] = useState({
    ip: '',
    username: '',
    password: '',
    key_path: '',
    command: '',
    commands: []
  });
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');
  const [mode, setMode] = useState('custom'); // 'custom' or 'inbuilt'


  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleCommandSelect = (command) => {
    if (mode === 'custom') {
      setForm({ ...form, command });
    } else {
      const updatedCommands = form.commands.includes(command)
        ? form.commands.filter(cmd => cmd !== command)
        : [...form.commands, command];
      setForm({ ...form, commands: updatedCommands });
    }
  };

  const handleSubmit = async e => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setOutput('');
    
    try {
      if (mode === 'custom') {
        const res = await axios.post('/api/remote_command', {
          ip: form.ip,
          username: form.username,
          password: form.password,
          key_path: form.key_path,
          command: form.command
        });
        setOutput(res.data.output || '');
        setError(res.data.error || '');
      } else {
        const res = await axios.post('/api/remote_commands', {
          ip: form.ip,
          username: form.username,
          password: form.password,
          key_path: form.key_path,
          commands: form.commands
        });
        setOutput(
          (res.data.results || []).map((r, i) => `# ${form.commands[i]}\n${r[1] || ''}${r[2] ? '\nError: ' + r[2] : ''}`).join('\n\n')
        );
        setError(res.data.error || '');
      }
    } catch (err) {
      setError('Failed to connect or execute command');
    } finally {
      setLoading(false);
    }
  };

  const getCategoryIcon = (category) => {
    const icons = {
      'Basic File & Directory Commands': <Folder />,
      'File Content Viewing': <FileCopy />,
      'File Permissions & Ownership': <Security />,
      'Archiving & Compression': <Storage />,
      'Process Management': <Monitor />,
      'User Management': <Settings />,
      'Networking': <NetworkCheck />,
      'Package Management (Ubuntu/Debian)': <Build />,
      'System Monitoring': <Monitor />,
      'Disk & Filesystem': <Storage />,
      'Text Editors': <Code />,
      'System Info': <Computer />,
      'Scripting & Automation': <Terminal />,
      'Fun Commands': <CodeIcon />
    };
    return icons[category] || <Code />;
  };

  return (
    <Box sx={{ p: 3, maxWidth: 1200, margin: '0 auto' }}>
      {/* Header */}
      <Box sx={{ display: 'flex', alignItems: 'center', mb: 3 }}>
        <IconButton onClick={() => navigate('/')} sx={{ mr: 2 }}>
          <ArrowBack />
        </IconButton>
        <Typography variant="h4" component="h1" sx={{ color: '#1976d2', fontWeight: 'bold' }}>
          SSH Remote Command
        </Typography>
      </Box>

      <Grid container spacing={3}>
        {/* Connection Form */}
        <Grid item xs={12} md={4}>
          <Paper elevation={3} sx={{ p: 3, height: 'fit-content' }}>
            <Typography variant="h6" gutterBottom sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
              <Computer sx={{ mr: 1 }} />
              Connection Settings
            </Typography>
            
            <Box component="form" onSubmit={handleSubmit} sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
              <TextField
                fullWidth
                label="IP Address"
                name="ip"
                value={form.ip}
                onChange={handleChange}
                required
                placeholder="192.168.1.100"
                size="small"
              />
              
              <TextField
                fullWidth
                label="Username"
                name="username"
                value={form.username}
                onChange={handleChange}
                required
                placeholder="ubuntu"
                size="small"
              />
              
              <TextField
                fullWidth
                label="Password"
                name="password"
                type="password"
                value={form.password}
                onChange={handleChange}
                placeholder="Leave empty if using key file"
                size="small"
              />
              
              <TextField
                fullWidth
                label="Private Key Path"
                name="key_path"
                value={form.key_path}
                onChange={handleChange}
                placeholder="C:\path\to\key.pem"
                size="small"
              />
              
              <Typography variant="caption" color="text.secondary" sx={{ fontStyle: 'italic' }}>
                Use either password OR key file for authentication
              </Typography>

              <Divider sx={{ my: 2 }} />

              {/* Mode Selection */}
              <FormControl fullWidth size="small">
                <InputLabel>Command Mode</InputLabel>
                <Select
                  value={mode}
                  onChange={(e) => setMode(e.target.value)}
                  label="Command Mode"
                >
                  <MenuItem value="custom">Custom Command</MenuItem>
                  <MenuItem value="inbuilt">Inbuilt Commands</MenuItem>
                </Select>
              </FormControl>

              {mode === 'custom' && (
                <TextField
                  fullWidth
                  label="Command"
                  name="command"
                  value={form.command}
                  onChange={handleChange}
                  required
                  placeholder="ls -la"
                  size="small"
                  multiline
                  rows={2}
                />
              )}

              <Button
                type="submit"
                variant="contained"
                startIcon={loading ? <CircularProgress size={20} /> : <PlayArrow />}
                disabled={loading}
                sx={{ mt: 2 }}
                fullWidth
              >
                {loading ? 'Executing...' : `Execute ${mode === 'custom' ? 'Command' : 'Commands'}`}
              </Button>
            </Box>
          </Paper>
        </Grid>

        {/* Command List */}
        <Grid item xs={12} md={8}>
          <Paper elevation={3} sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
              <ListIcon sx={{ mr: 1 }} />
              Available Commands
            </Typography>

            {mode === 'inbuilt' && (
              <Box sx={{ mb: 2 }}>
                <Typography variant="body2" color="text.secondary" sx={{ mb: 1 }}>
                  Selected Commands: {form.commands.length}
                </Typography>
                {form.commands.length > 0 && (
                  <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1, mb: 2 }}>
                    {form.commands.map((cmd, index) => (
                      <Chip
                        key={index}
                        label={cmd}
                        onDelete={() => handleCommandSelect(cmd)}
                        size="small"
                        color="primary"
                        variant="outlined"
                      />
                    ))}
                  </Box>
                )}
              </Box>
            )}

            <Box sx={{ maxHeight: 600, overflow: 'auto' }}>
              {INBUILT_COMMANDS.map((group) => (
                <Accordion key={group.label} sx={{ mb: 1 }}>
                  <AccordionSummary expandIcon={<ExpandMore />}>
                    <Box sx={{ display: 'flex', alignItems: 'center', width: '100%' }}>
                      {getCategoryIcon(group.label)}
                      <Typography sx={{ ml: 1, fontWeight: 'medium' }}>
                        {group.label}
                      </Typography>
                      <Chip
                        label={group.commands.length}
                        size="small"
                        sx={{ ml: 'auto' }}
                      />
                    </Box>
                  </AccordionSummary>
                  <AccordionDetails>
                    <List dense>
                      {group.commands.map((command) => (
                        <ListItem
                          key={command}
                          button
                          onClick={() => handleCommandSelect(command)}
                          sx={{
                            borderRadius: 1,
                            mb: 0.5,
                            backgroundColor: mode === 'custom' && form.command === command
                              ? 'primary.light'
                              : mode === 'inbuilt' && form.commands.includes(command)
                              ? 'primary.light'
                              : 'transparent',
                            '&:hover': {
                              backgroundColor: 'action.hover'
                            }
                          }}
                        >
                          <ListItemIcon>
                            <CodeIcon fontSize="small" />
                          </ListItemIcon>
                          <ListItemText
                            primary={command}
                            primaryTypographyProps={{
                              fontFamily: 'monospace',
                              fontSize: '0.875rem'
                            }}
                          />
                        </ListItem>
                      ))}
                    </List>
                  </AccordionDetails>
                </Accordion>
              ))}
            </Box>
          </Paper>
        </Grid>

        {/* Output */}
        {(output || error) && (
          <Grid item xs={12}>
            <Paper elevation={3} sx={{ p: 3 }}>
              <Typography variant="h6" gutterBottom>
                Command Output
              </Typography>
              
              {error && (
                <Alert severity="error" sx={{ mb: 2 }}>
                  {error}
                </Alert>
              )}
              
              {output && (
                <Box
                  component="pre"
                  sx={{
                    backgroundColor: '#f5f5f5',
                    p: 2,
                    borderRadius: 1,
                    maxHeight: 400,
                    overflow: 'auto',
                    fontFamily: 'monospace',
                    fontSize: '0.875rem',
                    border: '1px solid #e0e0e0'
                  }}
                >
                  {output}
                </Box>
              )}
            </Paper>
          </Grid>
        )}
      </Grid>
    </Box>
  );
}

export default RemoteCommandComponent; 