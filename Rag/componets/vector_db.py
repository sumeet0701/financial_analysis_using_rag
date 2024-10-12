from Rag.logger import logging
from Rag.exception import RagException
from Rag.constant import *
import os, sys
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.cohere import CohereEmbedding
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
            logging.info("embedding of Model loading is started...")

            model_name = self.model_name

            embed_model = CohereEmbedding(
                api_key=self.api_key,
                model_name = self.model_name
                input_type="search_document"

            )

            logging.info("embedding model is loadde. completed successfully..")
            return embed_model
        except Exception as e:
            logging.error("Error Embedding document:", exc_info=True)  # Log detailed error information
            raise RagException(e) from e
        

class VectorEmbeddingStoring:
    def __init__(self, collection, api_key, model_name):
        self.vector_db_path = VECTOR_DB_FILE_PATH
        self.client = chromadb.PersistentClient(path =self.vector_db_path)
        self.collection = self.client.get_or_create_collection(name = collection)
        self.embedder = Embedding(api_key, model_name)
    
    def saving_vector_database(self, nodes):
        try:
            logging.info("embedding of document is started...")
            embed_model = self.embedder.embedding_document()
            vector_store = ChromaVectorStore(chroma_collection = self.collection)
            storage_context = StorageContext.from_defaults(vector_store =  vector_store)
            index = VectorStoreIndex( 
                nodes,
                storage_context = storage_context,
                embed_model = embed_model
                
            )
            logging.info("Data is stored sucessfully in vector database....")
            return index
        except Exception as e:
            logging.error("Error Embedding document:", exc_info=True)  # Log detailed error information
            raise RagException(e) from e
    
    def loading_vector_database(self):
        try:
            logging.info("Loading vector embedding from database...")
            db = self.client
            embed_model = self.embedder.embedding_document()
            collection = db.get_or_create_collection(collection)
            vector_store = ChromaVectorStore(chroma_collection=collection)
            index = VectorStoreIndex.from_vector_store(
                vector_store,
                embed_model=embed_model
            )
            logging.info("vector embedding of the document retrived sucessfully")
            return index
        except Exception as e:
            logging.error("Error Embedding document:", exc_info=True)  # Log detailed error information
            raise RagException(e) from e
    




    





