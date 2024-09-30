import streamlit as st
from Rag.constant import *
from Rag.componets.web_scraping import WebScraper
from Rag.componets.chunking import Chunking
from Rag.componets.vector_db import Embedding
from Rag.pipeline.pipeline import Pipeline
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get('GOOGLE_API_KEY')
embedding_model = GOOGLE_EMBEEDING_MODEL 



def main():
    st.title("Company Data Scraper")

    # Input box with a placeholder to encourage input
    company_name = st.text_input("Enter the Company Name", placeholder="e.g., Reliance Industries")

    if st.button("Fetch Data"):
        if company_name:
            with st.spinner("Fetching data..."):
                # Construct the complete web page URL using the company name
                pipeline = Pipeline(company_name = company_name)
                data = pipeline.webscraper()

                #chunk = Chunking(api_key= api_key, embedding_model= embedding_model).chunking_document(documents=data, num_batches= 5)
                if data:
                    st.success("Data fetched successfully!")
                    for item in data:
                        st.write(item) 

                else:
                    st.error("Failed to fetch data. Please try again.")
        else:
            st.warning("Please enter a company name.")
    
    query = st.text_input("Enter")

if __name__ == "__main__":
    main()