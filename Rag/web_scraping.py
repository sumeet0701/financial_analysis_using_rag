# scraping the webpage using llama-index 
from logger import logging
from exception import RagException
from llama_index.readers.web import SimpleWebPageReader
import os
import sys


def webpage_scrape(path):
    logging.info("strating the data from the web page")
    try:
        documents = SimpleWebPageReader(html_to_text = True).load_data(
            [path]
        )
        logging.info("data is extracted from the web page successfully")
        return documents
    except Exception as e:
        raise RagException(e, sys) from e



document = webpage_scrape("https://ticker.finology.in/company/RELIANCE")
print(document)