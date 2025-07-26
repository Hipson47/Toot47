import os
from typing import Dict, List, Optional
from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.schema import Document

class VectorRAG:
    """A simple vector-based RAG system as fallback for GraphRAG."""
    
    def __init__(self, openai_api_key: str, data_dir: str = "./data", user_id: str = None):
        """
        Initialize VectorRAG with embeddings and vector store.
        
        Args:
            openai_api_key: OpenAI API key for LLM and embeddings
            data_dir: Directory containing documents to index
            user_id: User ID for creating user-specific vector store
        """
        self.openai_api_key = openai_api_key
        self.data_dir = data_dir
        self.user_id = user_id or "default"
        self.vectorstore = None
        self.qa_chain = None
        
        # Try OpenAI embeddings first, fallback to local
        try:
            self.embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        except Exception:
            # Fallback to local sentence transformers
            self.embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        
        self.llm = ChatOpenAI(
            temperature=0, 
            model_name="gpt-4o-mini",  # Use mini for cost efficiency
            openai_api_key=openai_api_key
        )
        
        # Initialize the system
        self._build_vectorstore()
        self._setup_qa_chain()
    
    def _build_vectorstore(self) -> None:
        """Build vector store from documents in data directory."""
        try:
            # Load documents
            loader = DirectoryLoader(
                self.data_dir, 
                glob="**/*.md", 
                show_progress=True
            )
            documents = loader.load()
            
            if not documents:
                print("No documents found in data directory")
                return
            
            # Split documents into chunks
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            texts = text_splitter.split_documents(documents)
            
            # Create user-specific vector store
            persist_dir = f"./chroma_db/user_{self.user_id}"
            self.vectorstore = Chroma.from_documents(
                documents=texts,
                embedding=self.embeddings,
                persist_directory=persist_dir
            )
            
            print(f"VectorRAG: Built vector store with {len(texts)} chunks")
            
        except Exception as e:
            print(f"Error building vector store: {e}")
            # Create empty user-specific vectorstore
            persist_dir = f"./chroma_db/user_{self.user_id}"
            self.vectorstore = Chroma(
                embedding_function=self.embeddings,
                persist_directory=persist_dir
            )
    
    def _setup_qa_chain(self) -> None:
        """Setup QA chain with retrieval."""
        if self.vectorstore:
            retriever = self.vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 3}
            )
            
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=retriever,
                return_source_documents=True
            )
    
    def ask(self, question: str) -> Dict:
        """
        Ask a question using vector RAG.
        
        Args:
            question: The question to ask
            
        Returns:
            Dictionary with answer and sources
        """
        if not self.qa_chain:
            return {
                "result": "Vector RAG system not properly initialized",
                "source_documents": []
            }
        
        try:
            response = self.qa_chain.invoke({"query": question})
            
            # Format response similar to GraphRAG
            return {
                "result": response.get("result", "No answer found"),
                "source_documents": [doc.page_content for doc in response.get("source_documents", [])],
                "method": "vector_rag"
            }
            
        except Exception as e:
            return {
                "result": f"Error in Vector RAG: {str(e)}",
                "source_documents": [],
                "method": "vector_rag"
            }
    
    def add_documents(self, documents: List[Document]) -> None:
        """Add new documents to the vector store."""
        if self.vectorstore:
            try:
                text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000,
                    chunk_overlap=200
                )
                texts = text_splitter.split_documents(documents)
                self.vectorstore.add_documents(texts)
                print(f"Added {len(texts)} new chunks to vector store")
            except Exception as e:
                print(f"Error adding documents: {e}") 