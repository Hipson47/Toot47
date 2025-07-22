# 1. Check for Python 3.12
Write-Host "Checking for Python 3.12..."
try {
    $pythonVersion = py -3.12 --version 2>&1
    if ($LASTEXITCODE -ne 0) { throw }
    Write-Host "Python 3.12 found: $pythonVersion"
} catch {
    Write-Error "Python 3.12 is not installed or not in PATH. Please install it and try again."
    exit 1
}

# 2. Check if Docker is running
Write-Host "Checking if Docker is running..."
docker info > $null 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Error "Docker is not running. Please start Docker Desktop and try again."
    # You can add a hint about the tray icon here if you want.
    exit 1
}
Write-Host "Docker is running."

# 3. Clone/Pull GraphRAG
$graphragDir = ".graphrag"
if (-not (Test-Path $graphragDir)) {
    Write-Host "Cloning Microsoft/GraphRAG..."
    git clone https://github.com/microsoft/graphrag.git $graphragDir
} else {
    Write-Host "Updating GraphRAG repository..."
    cd $graphragDir
    git pull
    cd ..
}

# 4. Create venv
$venvDir = Join-Path $graphragDir "venv"
if (-not (Test-Path $venvDir)) {
    Write-Host "Creating Python virtual environment..."
    py -3.12 -m venv $venvDir
}

# 5. Install dependencies
Write-Host "Installing dependencies..."
$pipExe = Join-Path $venvDir "Scripts" "pip.exe"
& $pipExe install -U pip
& $pipExe install -r (Join-Path $graphragDir "python" "requirements.txt")

# 6. Start Neo4j container
$containerName = "neo4j-graphrag"
$existingContainer = docker ps -a --filter "name=$containerName" --format "{{.Names}}"
if ($existingContainer -ne $containerName) {
    Write-Host "Starting Neo4j container..."
    docker run -d --name $containerName -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/password neo4j:5
} else {
    Write-Host "Neo4j container is already running."
}

# 7. Launch Streamlit demo
Write-Host "Launching Streamlit demo..."
$streamlitExe = Join-Path $venvDir "Scripts" "streamlit.exe"
$appPath = Join-Path $graphragDir "python" "app.py"
& $streamlitExe run $appPath
Start-Process "http://localhost:8501"

Write-Host "Setup complete." 