# Program: Retrieve information from web using semantic search approach

import requests
from bs4 import BeautifulSoup

# Website to scrape
url = "https://en.wikipedia.org/wiki/Data_science"

# Send HTTP request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract paragraph text
paragraphs = soup.find_all("p")

# Combine first few paragraphs
text_data = ""
for p in paragraphs[:5]:
    text_data += p.text

print("Extracted Information:\n")
print(text_data[:1000])  # Print first 1000 characters
