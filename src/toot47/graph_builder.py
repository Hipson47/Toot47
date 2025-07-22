import os
from pathlib import Path
from langchain_community.graphs import Neo4jGraph
from langchain_community.document_loaders import DirectoryLoader
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import ChatOpenAI
from .config import settings

def build_graph_from_documents(data_dir: str) -> tuple[int, int, list[str]]:
    """
    Builds the knowledge graph from documents in the specified directory.

    Args:
        data_dir: The path to the directory containing the documents.

    Returns:
        A tuple containing the number of nodes created, relationships created,
        and a list of processed file paths.
    """
    graph = Neo4jGraph(
        url=settings.NEO4J_URI,
        username=settings.NEO4J_USER,
        password=settings.NEO4J_PASS
    )
    graph.query("MATCH (n) DETACH DELETE n")  # Clear existing graph

    loader = DirectoryLoader(data_dir, glob="**/*.md", show_progress=True)
    documents = loader.load()
    
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o", openai_api_key=settings.OPENAI_API_KEY)
    llm_transformer = LLMGraphTransformer(llm=llm)

    graph_documents = llm_transformer.convert_to_graph_documents(documents)
    graph.add_graph_documents(graph_documents)

    nodes_created = sum(len(doc.nodes) for doc in graph_documents)
    relationships_created = sum(len(doc.relationships) for doc in graph_documents)
    files_processed = [str(Path(doc.metadata['source']).name) for doc in documents]

    return nodes_created, relationships_created, list(set(files_processed)) 