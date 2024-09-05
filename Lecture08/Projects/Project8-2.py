import requests
from datetime import datetime

def fetch_apod(api_key):
    """Fetch the Astronomy Picture of the Day from NASA's API."""
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Error occurred during requests to {url}: {err}")
        return None

def display_apod_info(apod_data):
    """Display the Astronomy Picture of the Day information."""
    if not apod_data:
        print("No APOD data found.")
        return
    
    title = apod_data.get('title', 'No Title')
    explanation = apod_data.get('explanation', 'No Explanation')
    media_type = apod_data.get('media_type', 'unknown')
    url = apod_data.get('url', 'No URL')
    date = apod_data.get('date', 'No Date')
    
    print(f"\nAstronomy Picture of the Day ({date}):\n")
    print(f"Title: {title}")
    print(f"Description: {explanation}")
    
    if media_type == 'image':
        print(f"Image URL: {url}")
    elif media_type == 'video':
        print(f"Video URL: {url}")
    else:
        print("Media type not recognized.")

if __name__ == "__main__":
    api_key = 'DEMO_KEY'  # Replace with your actual NASA API key
    print("Fetching Astronomy Picture of the Day...")
    apod_data = fetch_apod(api_key)
    
    if apod_data:
        display_apod_info(apod_data)
    else:
        print("Failed to retrieve APOD data.")
