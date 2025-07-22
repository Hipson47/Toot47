@echo off
title GraphRAG One-Click Setup (fixed)
setlocal ENABLEDELAYEDEXPANSION
pushd %~dp0                 :: ← pracuj w katalogu pliku .bat

::──────────────── 1. PREREQUISITES ────────────────
echo [CHECK] docker / git / python
where docker >nul 2>&1 || (
  echo [INSTALL] Docker Desktop via winget…
  winget install -e --id Docker.DockerDesktop || goto :wingetFail
  echo [INFO] Zrestartuj system i odpal skrypt ponownie.
  pause & exit /b
)
where git   >nul 2>&1 || winget install -e --id Git.Git           || goto :wingetFail
where python>nul 2>&1 || winget install -e --id Python.Python.3.12 || goto :wingetFail

::──────────────── 2. CLONE OR UPDATE REPO ─────────
if not exist graphrag (
  git clone https://github.com/microsoft/graphrag.git
) else (
  echo [UPDATE] pulling latest changes…
  git -C graphrag pull
)

::──────────────── 3. PYTHON VENV ──────────────────
cd graphrag
if not exist venv ( python -m venv venv )
call venv\Scripts\activate
python -m pip install -U pip
pip install graphrag streamlit neo4j openai

::──────────────── 4. NEO4J CONTAINER ──────────────
docker inspect neo4j-graphrag >nul 2>&1
if errorlevel 1 (
  echo [START] Neo4j container…
  docker run -d --name neo4j-graphrag -p7474:7474 -p7687:7687 ^
    -e NEO4J_AUTH=neo4j/test123 neo4j:5.19
)

::──────────────── 5. .ENV TEMPLATE ────────────────
if not exist .env (
  echo OPENAI_API_KEY=>> .env
  echo NEO4J_URI=bolt://localhost:7687>> .env
  echo NEO4J_USER=neo4j>> .env
  echo NEO4J_PASS=test123>> .env
  echo [WARN] Uzupełnij plik .env kluczem OpenAI!
)

::──────────────── 6. STREAMLIT DEMO ───────────────
echo [RUN] Streamlit demo → http://localhost:8501
start "" venv\Scripts\python.exe -m streamlit run ^
  samples\streamlit_demo\app.py --server.headless true

echo.
echo ============================================================
echo  Neo4j Browser        : http://localhost:7474  (neo4j/test123)
echo  Streamlit Chat Demo  : http://localhost:8501
echo ------------------------------------------------------------
echo  * Wrzuć PDF/MD w UI → automatycznie zląduje do katalogu data
echo  * Kliknij  „Re-index”, by przebudować graf
echo ============================================================
pause
exit /b

:wingetFail
echo [ERROR] Winget nie może zainstalować pakietu. Sprawdź log.
pause
endlocal
