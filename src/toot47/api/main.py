from fastapi import FastAPI, APIRouter, HTTPException, Request
from pydantic import BaseModel
from contextlib import asynccontextmanager
from toot47.qa import GraphAgent
from toot47.graph_builder import build_graph_from_documents
from toot47.config import settings
import os

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This code runs on startup
    print("Initializing GraphAgent...")
    try:
        # Check if the key was provided via prompt at startup
        if not settings.OPENAI_API_KEY:
            raise ValueError("OpenAI API key is missing.")

        graph_agent = GraphAgent(
            uri=settings.NEO4J_URI,
            user=settings.NEO4J_USER,
            password=settings.NEO4J_PASS,
            openai_api_key=settings.OPENAI_API_KEY
        )
        app.state.graph_agent = graph_agent
        print("GraphAgent initialized successfully.")
    except Exception as e:
        # If the agent can't be created, log it.
        # The app will start but endpoints requiring the agent will fail.
        print(f"FATAL: Could not initialize GraphAgent: {e}")
        app.state.graph_agent = None
    yield
    # This code runs on shutdown
    print("Closing resources...")

# --- Pydantic Models ---
class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    cypher_query: str | None = None

class BuildGraphResponse(BaseModel):
    status: str
    nodes_created: int
    relationships_created: int
    files_processed: list[str]

class HealthCheck(BaseModel):
    status: str = "OK"

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
    graph_agent = request.app.state.graph_agent
    if not graph_agent:
        raise HTTPException(status_code=503, detail="GraphAgent is not available. Check server logs for initialization errors.")
    try:
        result = graph_agent.ask(query.question)
        return QueryResponse(
            answer=result.get("result", "No answer found."),
            cypher_query=result.get("generated_query")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@api_router.post("/build-graph", response_model=BuildGraphResponse, tags=["Graph Management"])
async def build_graph() -> BuildGraphResponse:
    try:
        # Check if OpenAI API key is available
        if not settings.OPENAI_API_KEY:
            raise HTTPException(
                status_code=400, 
                detail="OpenAI API key is required. Please create a .env file in the project root with OPENAI_API_KEY=your_key_here"
            )
        
        data_path = "./data"
        if not os.path.exists(data_path) or not os.listdir(data_path):
            raise HTTPException(status_code=400, detail="Data directory is empty or does not exist.")
        
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