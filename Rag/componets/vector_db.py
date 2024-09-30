from Rag.logger import logging
from Rag.exception import RagException
import os, sys
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
import chromadb
from dotenv import load_dotenv

class DividingDataIntoNodes:
    def __init__(self,):
        pass
    def chunking_nodes():
        ...


class Embedding:

    def __init__(self, api_key, model_name):
        logging.info("Embedding of chunking data is started...")
        self.api_key = api_key
        self.model_name = model_name
    

    def embedding_document(self, documents):
        try:
        # get API key and create embeddings
            logging.info("embedding of documents is started...")

            model_name = self.model_name

            embed_model = GeminiEmbedding(
                model_name=model_name, 
                api_key=self.api_key, 
            )

            logging.info("embedding of documents is completed successfully..")
            return embed_model
        except Exception as e:
            logging.error("Error Embedding document:", exc_info=True)  # Log detailed error information
            raise RagException(e) from e
        






