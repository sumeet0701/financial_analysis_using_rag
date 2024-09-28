import streamlit as st
from Rag.web_scraping import WebScraper  # Assuming Rag.web_scraping provides WebScraper

# Define the web page URL template with a placeholder for the company name
WEBPAGE_URL_TEMPLATE = "https://ticker.finology.in/company/{}"

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

                if data:
                    st.success("Data fetched successfully!")
                    for item in data:
                        st.write(item)
                else:
                    st.error("Failed to fetch data. Please try again.")
        else:
            st.warning("Please enter a company name.")

if __name__ == "__main__":
    main()