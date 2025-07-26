from typing import Dict, Optional
from src.toot47.qa import GraphAgent
from src.toot47.vector_rag import VectorRAG

class HybridAgent:
    """Hybrid agent that tries GraphRAG first, then falls back to VectorRAG."""
    
    def __init__(self, neo4j_uri: str, neo4j_user: str, neo4j_pass: str, openai_api_key: str, data_dir: str = "./data"):
        """
        Initialize hybrid agent with both GraphRAG and VectorRAG.
        
        Args:
            neo4j_uri: Neo4j database URI
            neo4j_user: Neo4j username
            neo4j_pass: Neo4j password
            openai_api_key: OpenAI API key
            data_dir: Directory containing documents
        """
        self.openai_api_key = openai_api_key
        self.graph_agent = None
        self.vector_rag = None
        
        # Try to initialize GraphRAG
        try:
            print("Initializing GraphRAG...")
            self.graph_agent = GraphAgent(
                uri=neo4j_uri,
                user=neo4j_user,
                password=neo4j_pass,
                openai_api_key=openai_api_key
            )
            print("GraphRAG initialized successfully!")
        except Exception as e:
            print(f"GraphRAG initialization failed: {e}")
            self.graph_agent = None
        
        # Always initialize VectorRAG as backup
        try:
            print("Initializing VectorRAG...")
            self.vector_rag = VectorRAG(
                openai_api_key=openai_api_key,
                data_dir=data_dir
            )
            print("VectorRAG initialized successfully!")
        except Exception as e:
            print(f"VectorRAG initialization failed: {e}")
            self.vector_rag = None
    
    def ask(self, question: str) -> Dict:
        """
        Ask a question using hybrid approach.
        
        Tries GraphRAG first, falls back to VectorRAG if GraphRAG fails.
        
        Args:
            question: The question to ask
            
        Returns:
            Dictionary with answer and metadata about which method was used
        """
        # Try GraphRAG first
        if self.graph_agent:
            try:
                print("Trying GraphRAG...")
                response = self.graph_agent.ask(question)
                
                # Check if we got a meaningful response
                result = response.get("result", "")
                if result and result.strip() and "No answer found" not in result:
                    response["method"] = "graph_rag"
                    response["fallback_used"] = False
                    return response
                else:
                    print("GraphRAG returned empty/invalid result, trying VectorRAG...")
                    
            except Exception as e:
                print(f"GraphRAG error: {e}, trying VectorRAG...")
        
        # Fallback to VectorRAG
        if self.vector_rag:
            try:
                print("Using VectorRAG fallback...")
                response = self.vector_rag.ask(question)
                response["fallback_used"] = True
                return response
            except Exception as e:
                print(f"VectorRAG error: {e}")
                return {
                    "result": f"Both GraphRAG and VectorRAG failed. GraphRAG: {'Available' if self.graph_agent else 'Not available'}, VectorRAG: {str(e)}",
                    "method": "error",
                    "fallback_used": True
                }
        
        # Both systems failed
        return {
            "result": "Both GraphRAG and VectorRAG systems are unavailable. Please check system configuration.",
            "method": "error", 
            "fallback_used": True
        }
    
    def get_status(self) -> Dict:
        """Get status of both RAG systems."""
        return {
            "graph_rag_available": self.graph_agent is not None,
            "vector_rag_available": self.vector_rag is not None,
            "hybrid_functional": self.graph_agent is not None or self.vector_rag is not None
        } 