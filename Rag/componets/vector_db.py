from Rag.logger import logging
from Rag.exception import RagException
import os, sys
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
import chromadb
from dotenv import load_dotenv


class Embedding:

    def __init__(self, api_key, model_name):
        self.api_key = api_key
        self.model_name = model_name
    

    def embedding_document(self, documents):
        # get API key and create embeddings
        logging.info("embedding of documents is started...")

        model_name = self.model_name

        embed_model = GeminiEmbedding(
            model_name=model_name, 
            api_key=self.api_key, 
            title="this is a document"
        )

        embeddings = embed_model.get_text_embedding(documents)

        return embeddings
    




