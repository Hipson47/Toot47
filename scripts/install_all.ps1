# 1. Assert Admin Privileges
if (-Not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Start-Process PowerShell -Verb RunAs -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`""
    exit
}

# 2. Detect/Install Docker
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "Docker not found. Installing via winget..."
    winget install Docker.DockerDesktop --accept-package-agreements --accept-source-agreements
    Write-Warning "Docker has been installed. Please reboot your system and run this script again."
    pause
    exit
}

# 3. Ensure Docker Daemon is Up
Write-Host "Waiting for Docker daemon..."
$timeout = New-TimeSpan -Seconds 60
$stopwatch = [System.Diagnostics.Stopwatch]::StartNew()
while ($stopwatch.Elapsed -lt $timeout) {
    docker info >$null 2>$null
    if ($LASTEXITCODE -eq 0) { Write-Host "Docker is running."; break }
    Start-Sleep -Seconds 5
}
if ($stopwatch.Elapsed -ge $timeout) {
    Write-Error "Docker daemon did not start within 60 seconds. Please start Docker Desktop manually and re-run the script."
    pause
    exit
}

# 4. Detect/Install Python 3.12
py -3.12 --version 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Python 3.12 not found. Installing via winget..."
    winget install Python.Python.3.12 --accept-package-agreements --accept-source-agreements
    # Re-check after install attempt
    py -3.12 --version 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Python 3.12 installation failed. Please install it manually."
        pause
        exit
    }
}

# 5. Clone/Pull GraphRAG Repo
$graphragDir = "$env:USERPROFILE\.graphrag"
if (Test-Path $graphragDir) {
    Write-Host "Updating GraphRAG repository..."
    git -C $graphragDir pull
} else {
    Write-Host "Cloning Microsoft/GraphRAG..."
    git clone https://github.com/microsoft/graphrag.git $graphragDir
}

# 6. Setup Python Environment
$venvDir = Join-Path $graphragDir "venv"
py -3.12 -m venv $venvDir
$pipExe = Join-Path $venvDir "Scripts" "pip.exe"
& $pipExe install -U pip
$reqFile = Join-Path $graphragDir "python" "requirements.txt"
if (Test-Path $reqFile) {
    & $pipExe install -r $reqFile
} else {
    & $pipExe install graphrag streamlit neo4j openai
}

# 7. Start/Recreate Neo4j Container
$containerName = "neo4j-graphrag"
if (docker ps -a --format '{{.Names}}' | findstr "^$containerName$") {
    Write-Host "Recreating Neo4j container..."
    docker rm -f $containerName
}
docker run -d --name $containerName -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/password neo4j:5.19

# 8. Setup .env file
$envFile = Join-Path $graphragDir ".env"
$envExample = Join-Path $graphragDir ".env.example"
if ((-not (Test-Path $envFile)) -and (Test-Path $envExample)) {
    Copy-Item $envExample $envFile
    Write-Warning "An .env file was created. Please edit it and add your OPENAI_API_KEY."
    Invoke-Item $envFile
}

# 9. Launch Streamlit
Write-Host "Launching Streamlit demo..."
$streamlitExe = Join-Path $venvDir "Scripts" "streamlit.exe"
$appPy = Join-Path $graphragDir "python" "app.py"
Start-Process $streamlitExe -ArgumentList "run $appPy"
Start-Process "http://localhost:8501"

# 10. Summary
Write-Host "`n--- Setup Complete ---"
Write-Host "Streamlit demo: http://localhost:8501"
Write-Host "Neo4j Browser: http://localhost:7474 (user: neo4j, pass: password)"
pause 