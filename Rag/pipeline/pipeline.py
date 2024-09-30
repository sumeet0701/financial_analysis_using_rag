from Rag.componets.web_scraping import WebScraper
from Rag.componets.chunking import Chunking
from Rag.componets.vector_db import Embedding
from Rag.componets.vector_db import VectorEmbeddingStoring
from Rag.logger import logging
from Rag.exception import RagException
from Rag.constant import *

class Pipeline:

    def __init__(self, company_name):
        self.webpage_url = WEBPAGE_URL_TEMPLATE.format(company_name)
        self.chunk_size = CHUNK_SIZE
        self.chunk_overlap = CHUNK_OVERLAP
    def webscraper(self):
        web_scrapper = WebScraper(path= self.webpage_url)
        data = web_scrapper.scrape()
        return data
    
    def chunking(self, data):
        chunking_instance = Chunking()
        nodes = chunking_instance.chunking_using_recursive(
            documents= data,
            chunk_overlap= self.chunk_overlap,
            chunk_size= self.chunk_size
        )
        return nodes

    
    def vector_database_dumping(self, nodes):
        vector_embedding = VectorEmbeddingStoring(collection= "web_data")
        loading_data_disk = vector_embedding.saving_vector_database(nodes = nodes)
        loading_data_from_database = vector_embedding.loading_vector_database()
        return loading_data_from_database
    
    def RAG(self):...

    def main():
        data = Pipeline.webscraper()
        nodes = Pipeline.chunking(data= data)
        vector = Pipeline.vector_database_dumping(nodes= nodes)
        return vector
    


