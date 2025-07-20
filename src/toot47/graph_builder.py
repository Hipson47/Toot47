import os
from pathlib import Path
from langchain_community.graphs import Neo4jGraph
from langchain_community.document_loaders import DirectoryLoader
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import ChatOpenAI
from . import config

def build_graph(data_dir: str):
    """Builds the knowledge graph from documents in data_dir."""
    print(f"Building graph from documents in: {data_dir}")

    graph = Neo4jGraph(
        url=config.NEO4J_URI,
        username=config.NEO4J_USER,
        password=config.NEO4J_PASS
    )
    graph.query("MATCH (n) DETACH DELETE n") # Clear existing graph

    loader = DirectoryLoader(data_dir, glob="**/*.md")
    documents = loader.load()

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o", openai_api_key=config.OPENAI_API_KEY)
    llm_transformer = LLMGraphTransformer(llm=llm)

    graph_documents = llm_transformer.convert_to_graph_documents(documents)
    graph.add_graph_documents(graph_documents)

    print("Graph building complete.") 