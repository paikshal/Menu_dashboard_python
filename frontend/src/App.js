import React, { useState, createContext, useContext } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { Box, AppBar, Toolbar, Typography, Button, Container, IconButton } from '@mui/material';
import { Brightness4, Brightness7 } from '@mui/icons-material';

import Login from './components/Login';
import Dashboard from './components/Dashboard';
import SmsComponent from './components/SmsComponent';
import CallComponent from './components/CallComponent';
import InstagramComponent from './components/InstagramComponent';
import RemoteCommandComponent from './components/RemoteCommandComponent';
import WhatsAppComponent from './components/WhatsAppComponent';
import GmailComponent from './components/GmailComponent';


// Authentication Context
const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

// Theme Context
const ThemeContext = createContext();

export const useTheme = () => useContext(ThemeContext);

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState(null);
  const [mode, setMode] = useState('light');

  // Create theme based on mode
  const theme = createTheme({
    palette: {
      mode: mode,
      primary: {
        main: '#1976d2',
      },
      secondary: {
        main: '#dc004e',
      },
    },
  });

  const toggleColorMode = () => {
    setMode((prevMode) => (prevMode === 'light' ? 'dark' : 'light'));
  };

  const login = (userData) => {
    setIsAuthenticated(true);
    setUser(userData);
    localStorage.setItem('user', JSON.stringify(userData));
  };

  const logout = () => {
    setIsAuthenticated(false);
    setUser(null);
    localStorage.removeItem('user');
  };

  // Check if user is logged in on app start
  React.useEffect(() => {
    const savedUser = localStorage.getItem('user');
    if (savedUser) {
      setUser(JSON.parse(savedUser));
      setIsAuthenticated(true);
    }
  }, []);

  const ProtectedRoute = ({ children }) => {
    return isAuthenticated ? children : <Navigate to="/login" />;
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, user, login, logout }}>
      <ThemeContext.Provider value={{ mode, toggleColorMode }}>
        <ThemeProvider theme={theme}>
          <CssBaseline />
          <Router>
            <Box sx={{ flexGrow: 1 }}>
              {isAuthenticated && (
                <AppBar position="static">
                  <Toolbar>
                    <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                      Menu-Based Dashboard
                    </Typography>
                    <IconButton 
                      sx={{ ml: 1, mr: 2 }} 
                      onClick={toggleColorMode} 
                      color="inherit"
                      title={mode === 'light' ? 'Switch to Dark Mode' : 'Switch to Light Mode'}
                    >
                      {mode === 'dark' ? <Brightness7 /> : <Brightness4 />}
                    </IconButton>
                    <Button color="inherit" onClick={logout}>
                      Logout
                    </Button>
                  </Toolbar>
                </AppBar>
              )}
            
            <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
              <Routes>
                <Route path="/login" element={
                  isAuthenticated ? <Navigate to="/" /> : <Login />
                } />
                <Route path="/" element={
                  <ProtectedRoute>
                    <Dashboard />
                  </ProtectedRoute>
                } />
                <Route path="/sms" element={
                  <ProtectedRoute>
                    <SmsComponent />
                  </ProtectedRoute>
                } />
                <Route path="/call" element={
                  <ProtectedRoute>
                    <CallComponent />
                  </ProtectedRoute>
                } />
                <Route path="/instagram" element={
                  <ProtectedRoute>
                    <InstagramComponent />
                  </ProtectedRoute>
                } />
                <Route path="/remote" element={
                  <ProtectedRoute>
                    <RemoteCommandComponent />
                  </ProtectedRoute>
                } />
                <Route path="/whatsapp" element={
                  <ProtectedRoute>
                    <WhatsAppComponent />
                  </ProtectedRoute>
                } />
                <Route path="/gmail" element={
                  <ProtectedRoute>
                    <GmailComponent />
                  </ProtectedRoute>
                } />

              </Routes>
            </Container>
          </Box>
        </Router>
      </ThemeProvider>
        </ThemeContext.Provider>
    </AuthContext.Provider>
  );
}

export default App; 