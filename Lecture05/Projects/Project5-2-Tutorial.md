## **Project: Analyzing Movie Ratings**

### **Step 1: Install and Import Required Libraries**
Before starting, ensure the necessary libraries are installed and imported.

```python
import pandas as pd
import matplotlib.pyplot as plt
```

---

### **Step 2: Load the Dataset**
- The dataset should be in CSV format. If students don’t have one, they can use a sample dataset (e.g., `movies.csv`).
- The dataset might have columns like:
  - `Movie`: Name of the movie
  - `Genre`: Genre of the movie
  - `Rating`: User rating (e.g., on a scale of 1-10)

```python
# Load dataset
df = pd.read_csv("movies.csv")

# Display the first few rows
print(df.head())
```

---

### **Step 3: Understand the Dataset**
- Print basic information and check for missing values.

```python
# Check dataset info
print(df.info())

# Check for missing values
print(df.isnull().sum())
```

---

### **Step 4: Data Cleaning (If Necessary)**
- If there are missing values, handle them by either removing or filling them with a default value.

```python
# Drop rows with missing values
df.dropna(inplace=True)
```

- Ensure numerical values are in the correct format.

```python
# Convert rating to numeric type (if needed)
df["Rating"] = pd.to_numeric(df["Rating"])
```

---

### **Step 5: Calculate Average Ratings for Each Genre**
- Group by `Genre` and compute the average rating.

```python
# Compute average rating per genre
genre_avg = df.groupby("Genre")["Rating"].mean()

# Display results
print(genre_avg)
```

---

### **Step 6: Find the Highest and Lowest Rated Movies**
- Identify the best and worst-rated movies.

```python
# Find highest-rated movie
highest_rated = df.loc[df["Rating"].idxmax()]
print("Highest Rated Movie:")
print(highest_rated)

# Find lowest-rated movie
lowest_rated = df.loc[df["Rating"].idxmin()]
print("Lowest Rated Movie:")
print(lowest_rated)
```

---

### **Step 7: Visualizing the Data**
#### **1. Bar Chart: Average Rating Per Genre**
```python
# Plot bar chart of average ratings per genre
plt.figure(figsize=(10, 5))
genre_avg.sort_values().plot(kind="bar", color="skyblue")
plt.title("Average Movie Ratings by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.show()
```

#### **2. Histogram: Distribution of Ratings**
```python
# Plot histogram of ratings
plt.figure(figsize=(8, 5))
plt.hist(df["Rating"], bins=10, color="green", edgecolor="black", alpha=0.7)
plt.title("Distribution of Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Movies")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
```

---

### **Step 8: Summarize the Findings**
Encourage students to analyze their results:
- Which genre has the highest and lowest average rating?
- What is the most common rating range?
- What trends can be observed?

---

### **Step 9: Encourage Exploration**
- Ask students to come up with their own questions and write code to find answers. Example:
  - What is the average rating for movies released after a certain year (if the dataset has a `Year` column)?
  - What is the most common genre in the dataset?
  - Are there more highly rated movies or low-rated movies?

---

### **Step 10: Save and Share Results**
- Students can save their findings in a text or CSV file.

```python
# Save summary to a file
summary = f"Highest Rated Movie:\n{highest_rated}\n\nLowest Rated Movie:\n{lowest_rated}\n\nAverage Ratings by Genre:\n{genre_avg}"
with open("movie_analysis_summary.txt", "w") as file:
    file.write(summary)
```

---

## **Bonus: Add Interactivity**
- Allow users to input a genre and see its average rating.

```python
# Ask user for a genre
user_genre = input("Enter a genre: ").strip()
if user_genre in genre_avg.index:
    print(f"Average rating for {user_genre}: {genre_avg[user_genre]:.2f}")
else:
    print("Genre not found in dataset.")
```

---

## **Conclusion**
This project teaches students how to:
✅ Work with real-world datasets  
✅ Use pandas for data analysis  
✅ Perform statistical computations  
✅ Visualize data with matplotlib  
✅ Communicate findings effectively  
