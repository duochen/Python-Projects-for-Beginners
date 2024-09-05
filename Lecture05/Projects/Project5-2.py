import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (you can use a CSV file of movie ratings, genres, etc.)
# Sample CSV columns: 'title', 'genre', 'rating'
movies = pd.DataFrame({
    'title': ['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5'],
    'genre': ['Action', 'Comedy', 'Drama', 'Comedy', 'Action'],
    'rating': [7.8, 6.5, 9.0, 5.2, 8.3]
})

# Calculate average rating by genre
def average_rating_by_genre(data):
    return data.groupby('genre')['rating'].mean()

# Find the highest and lowest-rated movies
def highest_lowest_rated_movies(data):
    highest = data.loc[data['rating'].idxmax()]
    lowest = data.loc[data['rating'].idxmin()]
    return highest, lowest

# Visualize the average rating by genre
def visualize_ratings_by_genre(data):
    avg_ratings = average_rating_by_genre(data)
    avg_ratings.plot(kind='bar', title='Average Ratings by Genre', ylabel='Rating', xlabel='Genre')
    plt.show()

# Display the analysis
def movie_rating_analysis():
    print("Average Rating by Genre:")
    print(average_rating_by_genre(movies))

    highest, lowest = highest_lowest_rated_movies(movies)
    print("\nHighest Rated Movie:", highest['title'], "with a rating of", highest['rating'])
    print("Lowest Rated Movie:", lowest['title'], "with a rating of", lowest['rating'])

    print("\nVisualizing the average rating by genre:")
    visualize_ratings_by_genre(movies)

movie_rating_analysis()
