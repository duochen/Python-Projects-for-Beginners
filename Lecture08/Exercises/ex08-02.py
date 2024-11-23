import requests

url = 'https://example.com'
response = requests.get(url)
print(response.text)  # Print HTML content