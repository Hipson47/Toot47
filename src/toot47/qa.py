from langchain.chains import GraphQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI
from . import config

class GraphAgent:
    """A Graph RAG agent that answers questions based on a Neo4j knowledge graph."""

    def __init__(self):
        self.graph = Neo4jGraph(
            url=config.NEO4J_URI,
            username=config.NEO4J_USER,
            password=config.NEO4J_PASS
        )
        self.llm = ChatOpenAI(temperature=0, model_name="gpt-4o", openai_api_key=config.OPENAI_API_KEY)
        self.chain = GraphQAChain.from_llm(self.llm, graph=self.graph, verbose=True)

    def ask(self, question: str) -> str:
        """Asks a question to the Graph RAG chain."""
        result = self.chain.run(question)
        return result 