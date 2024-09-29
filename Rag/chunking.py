from Rag.logger import logging
from Rag.exception import RagException
from Rag.constant import *
from llama_index.core.node_parser import SemanticSplitterNodeParser
# from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.gemini import GeminiEmbedding
import math
import os, sys





class Chunking:
    def __init__(self, api_key, embedding_model):
        self.api_key = api_key
        self.embedding_model = embedding_model
    

    # def split_nodes_in_batches(self, nodes, num_batches):
    #     """Splits a list of nodes into the specified number of batches."""
    #     logging.info("spliting the extracted document into different batches...")
    #     try:
    #         batch_size = math.ceil(len(nodes) / num_batches)
    #         logging.info("successfully divided the document into batches")
    #         lst =[nodes[i:i + batch_size] for i in range(0, len(nodes), batch_size)]
    #         logging.info(f"{lst}")
    #         return lst

    #     except Exception as e:
    #         logging.error("Error splitting nodes into batches:", exc_info=True)  # Log detailed error information
    #         return []
    
    def spliting_document_into_batches(self, document, num_batches):
        logging.info("Spliting document into batches")
        try:
            lines = document.split('\n')
            batch_size = len(lines)/num_batches
            batches = [lines[i:i + batch_size] for i in range(0, len(lines), batch_size)]
            logging.info("Spliting document into batches is complete successfull")
            return batches
        except Exception as e:
            logging.error("Error chunking data:", exc_info=True)  # Log detailed error information
            return []
            
    def chunking_document(self, documents, num_batches):
        """Chunks the document using semantic chunking."""
        logging.info("Chunking document using semantic chunking methods")
        try:
            logging.info("Loading the Google Gemini embedding model....")
            embedding_model = GeminiEmbedding(
                model_name=self.embedding_model,  # Use the model name passed during class initialization
                api_key=self.api_key,
                title="Embedding the extracted documents",
            )

            # Initialize the splitter with the embedding model
            logging.info("Initializing the semantic splitter")
            splitter = SemanticSplitterNodeParser(
                buffer_size=10,
                breakpoint_percentile_threshold=95,
                embed_model=embedding_model,
            )

            # Split the documents into batches
            logging.info(f"Splitting the documents into {num_batches} batches")
            batch_documents = self.spliting_document_into_batches(documents, num_batches)

            nodes = []
            for idx, batch in enumerate(batch_documents):
                logging.info(f"{documents}")
                logging.info(f"Processing batch {idx + 1} of {len(batch_documents)}")
                batch_nodes = splitter.get_nodes_from_documents(batch, show_process=True)
                nodes.extend(batch_nodes)  # Correctly appending nodes from the batch

            logging.info(f"Chunking finished. Example content from 1st node: {nodes[0].get_content()}")

            return nodes

        except Exception as e:
            logging.error("Error chunking data:", exc_info=True)  # Log detailed error information
            return []































# def _splitting_nodes_in_batches(self, nodes, num_batches):
#     try:
#         self.nodes = nodes
#         self.num_batches = num_batches

#         batch_size = math.ceil(len(nodes)/num_batches)
#         return [nodes[i:i + batch_size] for i in range(0, len(nodes), batch_size)]

#     except Exception as e:
#         logging.error("splitting data into batches:", exc_info=True)  # Log detailed error information
#         return ""


# def chunking_document(documents, num_batch):
#     logging.info("Chunking document using semantic chunking methods")
#     try:
#         logging.info("loading the Google Gemini model embedding model....")
#         embedding_model = GeminiEmbedding(
#             model_name = GOOGLE_EMBEEDING_MODEL,
#             api_key = api_key,
#             title = "Embedding the extracted documents",
#         )

#         # splitting the text using semantic chunking
#         logging.info("chunking started")
#         splitter = SemanticSplitterNodeParser(
#             buffer_size = 10,
#             breakpoint_percentile_threshold=95,
#             embed_model=embedding_model,
#         )

#         # splitting the text into different batches:
#         batch_documents = _splitting_nodes_in_batches(nodes= documents, num_batches= num_batch)

#         nodes = []
#         for i in batch_documents:
#             nodes = splitter.get_nodes_from_documents(batch_documents,show_process = True)
#             nodes.append(nodes[i])
#         logging.info(f"chunking finished and 1st document found {nodes[1].get_content()}")

#         return nodes

#     except Exception as e:
#         logging.error("Error chunking data:", exc_info=True)  # Log detailed error information
#         return ""
    