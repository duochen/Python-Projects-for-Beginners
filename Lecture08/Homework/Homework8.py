import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape book reviews from a practice page
def scrape_reviews(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # List to store the scraped data
    data = []
    
    # Find all book review elements
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        # Extract book title
        book_title_tag = book.h3.a
        book_title = book_title_tag['title'] if book_title_tag else 'No Title'
        
        # Extract rating
        rating_tag = book.p
        rating_class = rating_tag['class'][1] if rating_tag and 'class' in rating_tag.attrs else 'No Rating'
        rating = rating_class.replace('star', '').replace('stars', '').strip()
        
        # Extract review text (simulate with a placeholder text as example)
        review_text = 'No Review Text'  # Placeholder, as this page does not contain reviews

        data.append([book_title, rating, review_text])
    
    return data

# Function to save data to a CSV file
def save_to_csv(data, filename):
    df = pd.DataFrame(data, columns=['Book Title', 'Rating', 'Review Text'])
    df.to_csv(filename, index=False)

# Function to analyze data
def analyze_data(filename):
    df = pd.read_csv(filename)
    
    # Convert ratings to numeric values for analysis
    df['Rating'] = df['Rating'].apply(lambda x: float(x) if x.isdigit() else 0.0)
    
    # Calculate average rating per book
    avg_ratings = df.groupby('Book Title')['Rating'].mean()
    
    # Count the number of reviews per book
    review_counts = df['Book Title'].value_counts()
    
    print("Average Ratings:")
    print(avg_ratings)
    print("\nReview Counts:")
    print(review_counts)

# Main function
def main():
    url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
    filename = 'book_reviews.csv'
    
    # Scrape data
    data = scrape_reviews(url)
    
    # Save data to CSV
    save_to_csv(data, filename)
    
    # Analyze data
    analyze_data(filename)

if __name__ == "__main__":
    main()
