from Rag.logger import logging
from Rag.exception import RagException
from Rag.constant import *
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
    

    def embedding_document(self):
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
        

class VectorEmbeddingStoring:
    def __init__(self, collection):
        self.vector_db_path = VECTOR_DB_FILE_PATH
        self.client = chromadb.PersistentClient(path =self.vector_db_path)
        self.collection = self.client.get_or_create_collection(name = collection)

    
    def saving_vector_database(self, nodes):
        vector_store = ChromaVectorStore(chroma_collection = self.collection)
        storage_context = storage_context.from_defaults(vector_store =  vector_store)
        index = vector_store( 
            nodes,
            storage_context = storage_context,
            embed_model = Embedding.embedding_document()
            
        )
        return index
    
    def loading_vector_database(self,):
        db = self.client
        collection = db.get_or_create_collection(collection)
        vector_store = ChromaVectorStore(chroma_collection=collection)
        index = VectorStoreIndex.from_vector_store(
            vector_store,
            embed_model=Embedding.embedding_document())
        
        return index
    




    





