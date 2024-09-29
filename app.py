import streamlit as st
from Rag.constant import *
from Rag.web_scraping import WebScraper
from Rag.chunking import Chunking
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get('GOOGLE_API_KEY')
embedding_model = GOOGLE_EMBEEDING_MODEL 
# Define the web page URL template with a placeholder for the company name
# WEBPAGE_URL_TEMPLATE = "https://ticker.finology.in/company/{}"

def main():
    st.title("Company Data Scraper")

    # Input box with a placeholder to encourage input
    company_name = st.text_input("Enter the Company Name", placeholder="e.g., Reliance Industries")

    if st.button("Fetch Data"):
        if company_name:
            with st.spinner("Fetching data..."):
                # Construct the complete web page URL using the company name
                webpage_url = WEBPAGE_URL_TEMPLATE.format(company_name)

                # Create a WebScraper instance for each scrape to avoid potential issues
                web_scraper = WebScraper(path= webpage_url)
                # Call the scrape method of the WebScraper instance
                data = web_scraper.scrape()
                chunk = Chunking(api_key= api_key, embedding_model= embedding_model).chunking_document(documents=data, num_batches= 5)
                if data:
                    st.success("Data fetched successfully!")
                    for item in data:
                        st.write(item)
                        st.write(chunk[1].get_content())
                else:
                    st.error("Failed to fetch data. Please try again.")
        else:
            st.warning("Please enter a company name.")

if __name__ == "__main__":
    main()