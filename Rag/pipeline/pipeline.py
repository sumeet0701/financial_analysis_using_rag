from Rag.componets.web_scraping import WebScraper
from Rag.componets.chunking import Chunking
from Rag.componets.vector_db import Embedding
from Rag.componets.vector_db import VectorEmbeddingStoring
from Rag.logger import logging
from Rag.exception import RagException
from Rag.constant import *
from dotenv import load_dotenv
import os

# api_key = load_dotenv("GOOGLE_API_KEY")
class Pipeline:

    def __init__(self, company_name):
        try:
            logging.info("Pipeline started.")
            self.webpage_url = WEBPAGE_URL_TEMPLATE.format(company_name)
            self.chunk_size = CHUNK_SIZE
            self.chunk_overlap = CHUNK_OVERLAP
            self.api_key = os.environ.get('GOOGLE_API_KEY')  # Store the API key
            self.model_name = GOOGLE_EMBEEDING_MODEL  # Store the model name
        except Exception as e:
            logging.error("Error Embedding document:", exc_info=True)  # Log detailed error information
            raise RagException(e) from e

    def webscraper(self):
        try:
            logging.info("web scraping of document pipeline started...")
            web_scrapper = WebScraper(path=self.webpage_url)
            data = web_scrapper.scrape()
            logging.info("web scrape pipeline completed successfully......")
            return data
        except Exception as e:
            logging.error("Error Embedding document:", exc_info=True)  # Log detailed error information
            raise RagException(e) from e
    
    def chunking(self, data):
        try: 
            logging.info("Chunking document of document pipeline started:", exc_info=True) # Log detailed error information
            chunking_instance = Chunking()
            nodes = chunking_instance.chunking_using_recursive(
                documents=data,
                chunk_overlap=self.chunk_overlap,
                chunk_size=self.chunk_size
            )
            logging.info("Chunking of documents completed successfully.....")
            return nodes
        except Exception as e:
            logging.error("Error Embedding document:", exc_info=True)  # Log detailed error information
            raise RagException(e) from e
        

    def vector_database_dumping(self, nodes):
        # Pass api_key and model_name when creating VectorEmbeddingStoring instance
        try:
            logging.info("vector database and embedding pipeline started sucessfully")
            vector_embedding = VectorEmbeddingStoring(
                collection="web_data",
                api_key=self.api_key,
                model_name=self.model_name
            )
            loading_data_disk = vector_embedding.saving_vector_database(nodes=nodes)
            loading_data_from_database = vector_embedding.loading_vector_database()
            logging.info("vector database and embedding completed successfully")
            return loading_data_from_database
        except Exception as e:
            logging.error("Error Embedding document:", exc_info=True)  # Log detailed error information
            raise RagException(e) from e
        
        
    def RAG(self):
        pass

    # Correct method definition with self
    def main(self):  
        data = self.webscraper()
        nodes = self.chunking(data=data)
        vector = self.vector_database_dumping(nodes=nodes)
        return vector
