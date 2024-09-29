from Rag.logger import loogging
from Rag.exception import RagException
import os, sys
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
import chromadb
from dotenv import load_dotenv
from Rag.componets.web_scraping import WebScraper



