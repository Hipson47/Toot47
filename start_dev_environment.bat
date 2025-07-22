@echo off
ECHO ========================================================
ECHO Starting Toot47 Development Environment...
ECHO ========================================================
ECHO.

ECHO [INFO] Stopping any old containers to prevent port conflicts...
docker-compose down
ECHO.

REM Step 1: Start Docker containers (Backend API and Neo4j)
ECHO [1/3] Starting Backend (API + Neo4j)...
start "Toot47 Backend" cmd /c "docker-compose up --build"

REM Step 2: Start the Frontend development server
ECHO [2/3] Starting Frontend (Next.js)...
start "Toot47 Frontend" cmd /c "cd frontend && npm run dev"

REM Step 3: Wait for services and open browser
ECHO [3/3] Waiting 15 seconds for services to initialize...
timeout /t 15 /nobreak > nul

ECHO Opening application in your browser at http://localhost:3000
start http://localhost:3000

exit