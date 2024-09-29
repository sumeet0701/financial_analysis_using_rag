from Rag.logger import logging
from Rag.exception import RagException
from Rag.constant import *
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from llama_index.core.node_parser import LangchainNodeParser
from llama_index.core.storage.docstore import SimpleDocumentStore

class Chunking:

    def __init__(self):
        pass
    
    def chunking_using_recursive(self, documents, chunk_size, chunk_overlap):
        """
        Chunk the document using recursive character splitter.
        
        Args:
            documents (list): A list of documents to chunk.
            chunk_size (int): Maximum size of each chunk.
            chunk_overlap (int): Overlap between consecutive chunks.

        Returns:
            list: A list of nodes (chunks) created from the document.
        """
        try:
            logging.info("chunking documents using recursive chunking")
            
            # Step 1: Initialize the recursive character splitter
            splitter = self._initialize_splitter(chunk_size, chunk_overlap)

            # Step 2: Parse the document and split into nodes
            nodes = self._parse_and_chunk_documents(splitter, documents)
            
            logging.info("chunking documents using recursive chunking is complete")
            return nodes
        except Exception as e:
            logging.error("Error splitting document:", exc_info=True)  # Log detailed error information
            raise RagException(e) from e

    def _initialize_splitter(self, chunk_size, chunk_overlap):
        """
        Initialize the RecursiveCharacterTextSplitter.

        Args:
            chunk_size (int): Maximum size of each chunk.
            chunk_overlap (int): Overlap between consecutive chunks.

        Returns:
            RecursiveCharacterTextSplitter: Initialized text splitter.
        """
        return RecursiveCharacterTextSplitter(
            chunk_overlap=chunk_overlap,
            chunk_size=chunk_size,
            is_separator_regex=True
        )
    
    def _parse_and_chunk_documents(self, splitter, documents):
        """
        Parse and chunk the documents into nodes using the splitter.

        Args:
            splitter (RecursiveCharacterTextSplitter): The initialized splitter.
            documents (list): A list of documents to chunk.

        Returns:
            list: A list of parsed nodes from the document.
        """
        try:
            logging.info("Initializing splitter")
            # Initialize the LangchainNodeParser with the splitter
            parser = LangchainNodeParser(splitter)
            
            # Parse and split the document into nodes (chunks)
            nodes = parser.get_nodes_from_documents(documents)
            logging.info("Node creation completed.")
            return nodes
        except Exception as e:
            logging.error("Error splitting nodes into batches:", exc_info=True)  # Log detailed error information
            raise RagException(e) from e
