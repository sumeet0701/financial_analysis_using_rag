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
                pipeline = Pipeline(company_name=company_name)
                data = pipeline.webscraper()

                if data:
                    st.success("Data fetched successfully!")
                    for item in data:
                        st.write(item)
                else:
                    st.error("Failed to fetch data. Please try again.")
        else:
            st.warning("Please enter a company name.")
    
    query = st.text_input("Enter your query to retrieve the data from database")
    if st.button("Submit"):
        if query:
            with st.spinner("Fetching data from the vector database..."):
                pipeline = Pipeline(company_name=company_name)
                vector_data = pipeline.main()  # Call main() correctly

                query_engine = vector_data.as_retriever()
                nodes = query_engine.retrieve(query)

                if nodes:
                    st.success("Data retrieved successfully")
                    st.write(nodes)
                else:
                    st.error("Failed to fetch data. Please try again.")
        else:
            st.warning("Please enter a query.")

if __name__ == "__main__":
    main()
