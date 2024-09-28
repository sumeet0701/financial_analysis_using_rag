from Rag.logger import logging
from Rag.exception import RagException
from Rag.constant import *
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import os, sys


def chunking_document(documents):
    logging.info("Chunking document using semantic chunking methods")
    try:
        logging.info("loading the hugging face embeddings model")
        embedding_model = HuggingFaceEmbedding(model_name = EMBEDDING_MODEL, trust_remote_code=True)

        # splitting the text using semantic chunking
        logging.info("chunking started")
        splitter = SemanticSplitterNodeParser(
            buffer_size = 1,
            breakpoint_percentile_threshold=95,
            embedding_model=embedding_model
        )

        nodes = splitter.get_nodes_from_documents(documents,show_process = True)
        logging.info(f"chunking finished and 1st document found {nodes[1].get_content()}")

        return nodes

    except Exception as e:
        logging.error("Error chunking data:", exc_info=True)  # Log detailed error information
        return ""
    