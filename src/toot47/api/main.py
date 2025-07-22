from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from toot47.qa import GraphAgent
from toot47.config import settings
from toot47.graph_builder import build_graph_from_documents
import os

# Define a simple response model for status checks
class HealthCheck(BaseModel):
    status: str = "OK"

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

# Create the main application instance
app = FastAPI(
    title="Toot47 GraphRAG API",
    description="API for interacting with the Toot47 knowledge graph.",
    version="1.0.0",
)

# Create a router for API endpoints
api_router = APIRouter()

# --- Agent Initialization ---
# Create a single, shared instance of the GraphAgent
try:
    graph_agent = GraphAgent(
        uri=settings.NEO4J_URI,
        user=settings.NEO4J_USER,
        password=settings.NEO4J_PASS,
        openai_api_key=settings.OPENAI_API_KEY
    )
except Exception as e:
    # If agent fails to initialize, the app can't function.
    # A more robust solution might involve a retry mechanism or a placeholder agent.
    graph_agent = None
    print(f"FATAL: Could not initialize GraphAgent: {e}")

@api_router.get("/health", response_model=HealthCheck, tags=["Status"])
async def get_health() -> HealthCheck:
    """
    Health check endpoint to confirm the API is running.
    """
    return HealthCheck(status="OK")

@api_router.post("/ask", response_model=QueryResponse, tags=["Query"])
async def ask_question(request: QueryRequest) -> QueryResponse:
    """Asks a question to the GraphRAG agent."""
    if not graph_agent:
        raise HTTPException(
            status_code=503,
            detail="GraphAgent is not available. Check server logs for initialization errors."
        )
    try:
        result = graph_agent.ask(request.question)
        return QueryResponse(
            answer=result.get("result", "No answer found."),
            cypher_query=result.get("generated_query") # Corrected key
        )
    except Exception as e:
        # Catch exceptions during the QA process
        raise HTTPException(status_code=500, detail=f"Error during question answering: {e}")

@api_router.post("/build-graph", response_model=BuildGraphResponse, tags=["Graph Management"])
async def build_graph() -> BuildGraphResponse:
    """
    Builds or updates the knowledge graph from documents in the './data' directory.
    """
    try:
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
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Welcome to the Toot47 API. Visit /docs for documentation."}

app.include_router(api_router, prefix="/api/v1") 