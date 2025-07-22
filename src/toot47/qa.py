from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI
from .config import settings

class GraphAgent:
    """A Graph RAG agent that answers questions based on a Neo4j knowledge graph."""

    def __init__(self):
        graph = Neo4jGraph(
            url=settings.NEO4J_URI,
            username=settings.NEO4J_USER,
            password=settings.NEO4J_PASS
        )
        llm = ChatOpenAI(temperature=0, model_name="gpt-4o", openai_api_key=settings.OPENAI_API_KEY)
        self.chain = GraphCypherQAChain.from_llm(
            llm, graph=graph, verbose=True
        )

    def ask(self, question: str) -> str:
        """Asks a question to the Graph RAG chain."""
        result = self.chain.invoke({"query": question})
        return result['result'] 