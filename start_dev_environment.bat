@echo off
ECHO ========================================================
ECHO Starting Toot47 Development Environment...
ECHO ========================================================
ECHO.

ECHO [INFO] This script will now stop any existing containers
ECHO        defined in docker-compose.yml to free up ports.
ECHO.

REM Step 0: Stop and remove existing containers to prevent port conflicts
docker-compose down

REM Step 1: Start Docker containers (Backend API and Neo4j) in a new window
ECHO [1/3] Starting Docker containers (Backend + Database)...
start "Toot47 Backend" cmd /c "docker-compose up --build"

REM Step 2: Start the Frontend development server in a new window
ECHO [2/3] Starting Frontend (Next.js development server)...
start "Toot47 Frontend" cmd /c "cd frontend && npm run dev"

REM Step 3: Wait for services to initialize and open the browser
ECHO [3/3] Waiting 15 seconds for services to start...
ECHO You can close the other terminal windows to stop the servers.
timeout /t 15 /nobreak > nul

ECHO Opening application in your browser at http://localhost:3000
start http://localhost:3000

exit