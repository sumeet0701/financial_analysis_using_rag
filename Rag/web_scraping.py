# scraping the webpage using llama-index 
from Rag.logger import logging
from Rag.exception import RagException
from llama_index.readers.web import SimpleWebPageReader
import os
import sys


class WebScraper:  # Corrected class name for clarity
    """
    This class represents a web scraper with functionalities for loading data from web pages.
    """

    def __init__(self, path: str):
        """
        Initializes the WebScraper instance with the path to the web page.

        Args:
            path (str): The path (URL) to the web page to scrape.
        """
        self.path = path

    def scrape(self) -> str:
        """
        Scrapes data from the specified web page and returns it as a string.

        Returns:
            str: The extracted data from the web page, or an empty string if an error occurs.
        """

        logging.info("Starting data scraping from the web page...")

        try:
             # Context manager for resource management
            documents = SimpleWebPageReader(html_to_text= True).load_data([self.path])
            logging.info("Data successfully extracted from the web page.")
            # logging.info(f"data type of document:{type(documents)}")
            return documents  # Remove potential leading/trailing whitespace
        except Exception as e:
            logging.error("Error scraping data:", exc_info=True)  # Log detailed error information
            return ""  # Return empty string on error

