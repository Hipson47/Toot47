from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI

class GraphAgent:
    """A Graph RAG agent that answers questions based on a Neo4j knowledge graph."""

    def __init__(self, uri: str, user: str, password: str, openai_api_key: str):
        """
        Initializes the GraphAgent.

        Args:
            uri: The URI for the Neo4j database.
            user: The username for the Neo4j database.
            password: The password for the Neo4j database.
            openai_api_key: The API key for the OpenAI service.
        """
        graph = Neo4jGraph(url=uri, username=user, password=password)
        llm = ChatOpenAI(temperature=0, model_name="gpt-4o", openai_api_key=openai_api_key)
        self.chain = GraphCypherQAChain.from_llm(
            llm, graph=graph, verbose=True, return_generated_query=True
        )

    def ask(self, question: str) -> dict:
        """
        Asks a question to the Graph RAG chain.

        Args:
            question: The question to ask.

        Returns:
            A dictionary containing the answer and the generated Cypher query.
        """
        return self.chain.invoke({"query": question}) 