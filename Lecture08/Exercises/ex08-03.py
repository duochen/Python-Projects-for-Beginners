import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)
print(response.text)  # Print HTML content
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())  # Pretty-print the HTML content

