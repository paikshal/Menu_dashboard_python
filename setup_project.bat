@echo off
echo ========================================
echo    Menu-Based Dashboard Setup
echo ========================================
echo.

echo Step 1: Setting up environment variables...
python setup_env.py
echo.

echo Step 2: Checking for security issues...
python github_safety_check.py
echo.

echo Step 3: Installing Python dependencies...
pip install -r requirements.txt
echo.

echo Step 4: Installing Node.js dependencies...
cd frontend
npm install
cd ..
echo.

echo Step 5: Starting the application...
echo.
echo Starting Python backend...
start "Backend Server" cmd /k "python app.py"
echo.

echo Starting React frontend...
cd frontend
start "Frontend Server" cmd /k "npm start"
cd ..
echo.

echo ========================================
echo    Setup Complete!
echo ========================================
echo.
echo Your application should now be running:
echo - Backend: http://localhost:5000
echo - Frontend: http://localhost:3000
echo.
echo Press any key to exit...
pause > nul 