# scripts/install_all.ps1

# --- CONFIGURATION ---
$env:PYTHON_VERSION = "3.12"
$env:PYTHON_PATH = "python" # Assumes python is in the system PATH
$env:NEO4J_CONTAINER_NAME = "neo4j-graphrag"
$env:NEO4J_IMAGE = "neo4j:5.20.0"
$env:NEO4J_PASSWORD = "password" # Do not use this in production
$env:NEO4J_BOLT_PORT = "7687"
$env:NEO4J_HTTP_PORT = "7474"

# --- SCRIPT LOGIC ---
# Use $PSScriptRoot for robust pathing relative to the script's location
$scriptPath = $PSScriptRoot
$rootPath = Split-Path -Path $scriptPath -Parent
Write-Host "Project root identified as: $rootPath"

# Move the system prompt file as per the plan
$promptSource = Join-Path -Path $rootPath -ChildPath "prompts/system.md"
$promptDestination = Join-Path -Path $rootPath -ChildPath "system_prompt.md"
if (Test-Path $promptSource) {
    Write-Host "Moving system prompt from $promptSource to $promptDestination..."
    if (Test-Path $promptDestination) {
        Remove-Item $promptDestination -Force
    }
    Move-Item -Path $promptSource -Destination $promptDestination
    Write-Host "System prompt moved successfully."
} else {
    Write-Host "System prompt already at the new location or not found at the old one. Skipping move."
}

# 1. Check for Docker
Write-Host "[1/6] Checking for Docker..."
$dockerStatus = docker info -f "{{.ServerVersion}}" 2>$null
if ($? -and $dockerStatus) {
    Write-Host "✅ Docker is running (Version: $dockerStatus)."
} else {
    Write-Error "❌ Docker is not running or not installed. Please start Docker Desktop and try again."
    exit 1
}

# 2. Check for Python
Write-Host "[2/6] Checking for Python version..."
try {
    $pythonVersionOutput = & $env:PYTHON_PATH --version 2>&1
    if ($pythonVersionOutput -match "$($env:PYTHON_VERSION)") {
        Write-Host "✅ Python $($env:PYTHON_VERSION) found."
    } else {
        Write-Warning "⚠️ Found Python version: $pythonVersionOutput. Expected $($env:PYTHON_VERSION). Compatibility issues may arise."
    }
} catch {
    Write-Error "❌ Python command '$($env:PYTHON_PATH)' not found. Please install Python $($env:PYTHON_VERSION) and ensure it's in your system's PATH."
    exit 1
}

# 3. Clone or update the GraphRAG repository
$graphRagPath = Join-Path -Path $rootPath -ChildPath ".graphrag"
Write-Host "[3/6] Setting up Microsoft GraphRAG repository in '$graphRagPath'..."
if (-not (Test-Path -Path $graphRagPath)) {
    Write-Host "Cloning repository..."
    git clone https://github.com/microsoft/graphrag.git $graphRagPath
} else {
    Write-Host "Repository exists. Pulling latest changes..."
    git -C $graphRagPath pull
}
Write-Host "✅ GraphRAG repository is ready."

# 4. Create virtual environment and install dependencies
$venvPath = Join-Path -Path $graphRagPath -ChildPath "venv"
Write-Host "[4/6] Setting up Python virtual environment..."
if (-not (Test-Path -Path $venvPath)) {
    Write-Host "Creating new virtual environment in '$venvPath'..."
    & $env:PYTHON_PATH -m venv $venvPath
} else {
    Write-Host "Virtual environment already exists."
}

Write-Host "Installing dependencies... (This may take a few minutes)"
& "$($venvPath)/Scripts/python.exe" -m pip install --upgrade pip
& "$($venvPath)/Scripts/python.exe" -m pip install -r (Join-Path -Path $graphRagPath -ChildPath "requirements.txt")
Write-Host "✅ Python dependencies are installed."

# 5. Start Neo4j Container
Write-Host "[5/6] Setting up Neo4j container..."
$container = docker ps -a --filter "name=$($env:NEO4J_CONTAINER_NAME)" --format "{{.Names}}"
if ($container) {
    Write-Host "Container '$($env:NEO4J_CONTAINER_NAME)' already exists. Ensuring it is running..."
    docker start $env:NEO4J_CONTAINER_NAME | Out-Null
} else {
    Write-Host "Creating and starting new Neo4j container '$($env:NEO4J_CONTAINER_NAME)'..."
    docker run -d --name $env:NEO4J_CONTAINER_NAME -p "$($env:NEO4J_HTTP_PORT):7474" -p "$($env:NEO4J_BOLT_PORT):7687" --env NEO4J_AUTH="neo4j/$($env:NEO4J_PASSWORD)" $env:NEO4J_IMAGE | Out-Null
}

# Wait a moment for Neo4j to initialize
Write-Host "Waiting for Neo4j to become available..."
Start-Sleep -Seconds 15 # Increased wait time for stability
Write-Host "✅ Neo4j container is running."

# 6. Run Streamlit Demo
Write-Host "[6/6] Starting Streamlit demo application..."
$streamlitAppPath = Join-Path -Path $graphRagPath -ChildPath "graphrag/query/app.py"
if (-not (Test-Path -Path $streamlitAppPath)) {
    Write-Error "❌ Streamlit entry point not found at '$streamlitAppPath'. The repository structure may have changed."
    exit 1
}

# The working directory needs to be the root of the graphrag repo for it to find its modules.
Set-Location $graphRagPath
Start-Process -FilePath "$($venvPath)/Scripts/streamlit.exe" -ArgumentList "run", "query/app.py"
Start-Process "http://localhost:8501"

Write-Host "✅ Setup complete. Streamlit demo should now be running and opening in your browser."