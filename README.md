# Toot47

GraphRAG project.

## Quick Start (Automated Installer)

For a fully automated setup, run the one-click installer which will handle all dependencies (Python, Docker) and configuration for you.

**Double-click `scripts/install_all.bat` (requires Administrator privileges).**

---

### Manual Setup

1.  **Install Git Hooks (one-time setup):**
    After cloning the repository, run one of the following scripts to install the pre-commit hooks. This will help ensure code quality and prevent committing secrets.
    -   For Windows: `scripts\install_hooks.ps1`
    -   For macOS/Linux: `bash scripts/install_hooks.sh`

2.  **Run the Demo:**
    Simply double-click the `scripts/setup_graph_rag.bat` file to set up and launch the GraphRAG demo.

3.  **Access Neo4j Browser:**
    Open your browser and navigate to [http://localhost:7474](http://localhost:7474).
    Connect with username `neo4j` and password `password`. 