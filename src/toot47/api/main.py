from fastapi import FastAPI, APIRouter, HTTPException, Request, UploadFile, File, Form
from pydantic import BaseModel
from contextlib import asynccontextmanager
from src.toot47.qa import GraphAgent
from src.toot47.hybrid_agent import HybridAgent
from src.toot47.graph_builder import build_graph_from_documents
from src.toot47.config import settings
import os
import shutil
from pathlib import Path

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This code runs on startup
    print("Initializing Hybrid RAG Agent...")
    try:
        # Check if the key was provided via prompt at startup
        if not settings.OPENAI_API_KEY:
            raise ValueError("OpenAI API key is missing.")

        hybrid_agent = HybridAgent(
            neo4j_uri=settings.NEO4J_URI,
            neo4j_user=settings.NEO4J_USER,
            neo4j_pass=settings.NEO4J_PASS,
            openai_api_key=settings.OPENAI_API_KEY,
            data_dir="./data"
        )
        app.state.hybrid_agent = hybrid_agent
        print("Hybrid RAG Agent initialized successfully.")
        
        # Log status
        status = hybrid_agent.get_status()
        print(f"System status: {status}")
        
    except Exception as e:
        # If the agent can't be created, log it.
        print(f"FATAL: Could not initialize Hybrid Agent: {e}")
        app.state.hybrid_agent = None
    yield
    # This code runs on shutdown
    print("Closing resources...")

# --- Pydantic Models ---
class QueryRequest(BaseModel):
    question: str
    user_id: str

class QueryResponse(BaseModel):
    answer: str
    cypher_query: str | None = None
    method: str | None = None
    fallback_used: bool | None = None
    source_documents: list[str] | None = None

class BuildGraphResponse(BaseModel):
    status: str
    nodes_created: int
    relationships_created: int
    files_processed: list[str]

class HealthCheck(BaseModel):
    status: str = "OK"

class SystemStatus(BaseModel):
    status: str = "OK"
    graph_rag_available: bool
    vector_rag_available: bool
    hybrid_functional: bool

class FileUploadResponse(BaseModel):
    status: str
    filename: str
    size: int
    message: str

# Create the main application instance with the lifespan manager
app = FastAPI(
    title="Toot47 GraphRAG API",
    description="API for interacting with the Toot47 knowledge graph.",
    version="1.0.0",
    lifespan=lifespan,
)

api_router = APIRouter()

@api_router.get("/health", response_model=HealthCheck, tags=["Status"])
async def get_health() -> HealthCheck:
    return HealthCheck(status="OK")

@api_router.post("/ask", response_model=QueryResponse, tags=["Query"])
async def ask_question(request: Request, query: QueryRequest) -> QueryResponse:
    # Create user-specific hybrid agent
    try:
        user_data_dir = f"./data/users/{query.user_id}"
        os.makedirs(user_data_dir, exist_ok=True)
        
        hybrid_agent = HybridAgent(
            neo4j_uri=settings.NEO4J_URI,
            neo4j_user=settings.NEO4J_USER,
            neo4j_pass=settings.NEO4J_PASS,
            openai_api_key=settings.OPENAI_API_KEY,
            data_dir=user_data_dir,
            user_id=query.user_id
        )
        
        result = hybrid_agent.ask(query.question)
        return QueryResponse(
            answer=result.get("result", "No answer found."),
            cypher_query=result.get("generated_query"),
            method=result.get("method"),
            fallback_used=result.get("fallback_used"),
            source_documents=result.get("source_documents", [])
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@api_router.get("/status", response_model=SystemStatus, tags=["Status"])
async def get_system_status(request: Request) -> SystemStatus:
    hybrid_agent = request.app.state.hybrid_agent
    if not hybrid_agent:
        return SystemStatus(
            status="Error",
            graph_rag_available=False,
            vector_rag_available=False,
            hybrid_functional=False
        )
    
    status = hybrid_agent.get_status()
    return SystemStatus(
        status="OK" if status["hybrid_functional"] else "Degraded",
        graph_rag_available=status["graph_rag_available"],
        vector_rag_available=status["vector_rag_available"],
        hybrid_functional=status["hybrid_functional"]
    )

@api_router.post("/upload-file", response_model=FileUploadResponse, tags=["File Management"])
async def upload_file(
    file: UploadFile = File(...),
    user_id: str = Form(...)
) -> FileUploadResponse:
    try:
        # Validate file type
        allowed_extensions = {".md", ".pdf"}
        file_extension = Path(file.filename or "").suffix.lower()
        
        if file_extension not in allowed_extensions:
            raise HTTPException(
                status_code=400,
                detail=f"File type {file_extension} not supported. Only .md and .pdf files are allowed."
            )
        
        # Create user-specific directory
        user_data_dir = Path(f"./data/users/{user_id}")
        user_data_dir.mkdir(parents=True, exist_ok=True)
        
        # Save file
        file_path = user_data_dir / (file.filename or "uploaded_file")
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return FileUploadResponse(
            status="success",
            filename=file.filename or "uploaded_file",
            size=file_path.stat().st_size,
            message=f"File uploaded successfully to user {user_id} knowledge base"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")

@api_router.post("/build-graph", response_model=BuildGraphResponse, tags=["Graph Management"])
async def build_graph(user_id: str = None) -> BuildGraphResponse:
    try:
        # Check if OpenAI API key is available
        if not settings.OPENAI_API_KEY:
            raise HTTPException(
                status_code=400, 
                detail="OpenAI API key is required. Please create a .env file in the project root with OPENAI_API_KEY=your_key_here"
            )
        
        # Use user-specific or global data path
        if user_id:
            data_path = f"./data/users/{user_id}"
        else:
            data_path = "./data"
            
        if not os.path.exists(data_path) or not os.listdir(data_path):
            raise HTTPException(status_code=400, detail=f"Data directory {data_path} is empty or does not exist.")
        
        nodes, rels, files = build_graph_from_documents(data_path)
        return BuildGraphResponse(
            status="Graph built successfully",
            nodes_created=nodes,
            relationships_created=rels,
            files_processed=files
        )
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"Build graph error: {error_details}")
        raise HTTPException(status_code=500, detail=f"Error building graph: {str(e)}")

@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Welcome to the Toot47 API. Visit /docs for documentation."}

app.include_router(api_router, prefix="/api/v1") 