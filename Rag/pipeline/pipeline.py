from Rag.componets.web_scraping import WebScraper
from Rag.componets.chunking import Chunking
from Rag.componets.vector_db import Embedding
from Rag.componets.vector_db import VectorEmbeddingStoring
from Rag.logger import logging
from Rag.exception import RagException
from Rag.constant import *

class Pipeline:

    def __init__(self, company_name, api_key, model_name):
        self.webpage_url = WEBPAGE_URL_TEMPLATE.format(company_name)
        self.chunk_size = CHUNK_SIZE
        self.chunk_overlap = CHUNK_OVERLAP
        self.api_key = api_key  # Store the API key
        self.model_name = model_name  # Store the model name

    def webscraper(self):
        web_scrapper = WebScraper(path=self.webpage_url)
        data = web_scrapper.scrape()
        return data
    
    def chunking(self, data):
        chunking_instance = Chunking()
        nodes = chunking_instance.chunking_using_recursive(
            documents=data,
            chunk_overlap=self.chunk_overlap,
            chunk_size=self.chunk_size
        )
        return nodes

    def vector_database_dumping(self, nodes):
        # Pass api_key and model_name when creating VectorEmbeddingStoring instance
        vector_embedding = VectorEmbeddingStoring(
            collection="web_data",
            api_key=self.api_key,
            model_name=self.model_name
        )
        loading_data_disk = vector_embedding.saving_vector_database(nodes=nodes)
        loading_data_from_database = vector_embedding.loading_vector_database()
        return loading_data_from_database
    
    def RAG(self):
        pass

    # Correct method definition with self
    def main(self):  
        data = self.webscraper()
        nodes = self.chunking(data=data)
        vector = self.vector_database_dumping(nodes=nodes)
        return vector
