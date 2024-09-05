### Python Project 2: Web Scraping - "NASA Astronomy Picture of the Day Scraper"

#### **Project Description:**
Students will build a web scraper that fetches information about the Astronomy Picture of the Day (APOD) from NASA’s API. The program will retrieve the image or video URL, title, and description, and then display this information to the user. This project introduces students to working with APIs and parsing JSON data.

#### **Learning Objectives:**
- Learning how to make API requests using Python (`requests`).
- Parsing JSON responses from APIs.
- Handling API keys and understanding rate limits.
- Structuring and displaying data retrieved from an API.

#### **Extensions:**
- Implement a feature to save the daily image to a local directory.
- Create a GUI using `tkinter` to display the image and description in a window.
- Add functionality to retrieve images from previous dates by adjusting the API request.

#### **Python Solution:**
To use the NASA APOD API, you’ll need an API key. You can obtain one for free from the [NASA API website](https://api.nasa.gov/). Replace `'DEMO_KEY'` in the code with your actual API key.

#### **Explanation:**

1. **API Request:**
   - The `fetch_apod` function makes a GET request to NASA’s APOD API using the provided API key and retrieves the response in JSON format.

2. **Data Parsing:**
   - The `display_apod_info` function extracts relevant information from the JSON response, including the title, description, media type (image or video), URL, and date.

3. **Output:**
   - The script prints the title, description, and URL of the media (image or video). If the media type is not recognized, it will handle it accordingly.

#### **Running the Script:**

1. **Install Required Libraries:**
   - Ensure you have the `requests` library installed:
     ```bash
     pip install requests
     ```

2. **Save and Run the Script:**
   - Save the script to a file, e.g., `apod_scraper.py`.
   - Run the script:
     ```bash
     python apod_scraper.py
     ```

3. **Output:**
   - The script will display the Astronomy Picture of the Day’s title, description, and URL.

**Note:** Remember to replace `'DEMO_KEY'` with your actual API key. If you need to display images or videos, you can enhance the script by integrating it with a GUI library or a web application framework to show the media directly.

This project not only gives students a taste of working with APIs but also provides interesting and up-to-date content related to space science.