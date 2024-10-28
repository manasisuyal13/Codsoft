import pandas as pd

# Load the movies metadata
movies_df = pd.read_csv('C:/Users/Manasi Suyal/the-movies-dataset/movies_metadata.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(movies_df.head())

# Display basic information about the dataset
print("\nBasic information about the dataset:")
print(movies_df.info())

# List available genres (optional for user reference)
print("\nAvailable genres (examples): Action, Comedy, Drama, Horror, Thriller, Romance")

# Ask the user for their preferred genre
preferred_genre = input("\nEnter your preferred movie genre: ")

# Ask the user for minimum rating
min_rating = float(input("Enter the minimum rating (0-10): "))

# Ask the user for the release year range
min_year = int(input("Enter the minimum release year (e.g., 2000): "))
max_year = int(input("Enter the maximum release year (e.g., 2024): "))

movies_df = movies_df[movies_df['release_date'].notna()]

# Filter the dataset based on the user's preferences
filtered_movies = movies_df[
    movies_df['genres'].str.contains(preferred_genre, case=False, na=False) &
    (movies_df['vote_average'] >= min_rating) &
    (movies_df['release_date'].str[:4].astype(int).between(min_year, max_year))
]

# Display the filtered results
if not filtered_movies.empty:
    print(f"\nMovies in the genre '{preferred_genre}' with a minimum rating of {min_rating} and released between {min_year} and {max_year}:")
    print(filtered_movies[['title', 'genres', 'release_date', 'vote_average']].head(10))
else:
    print(f"\nNo movies found matching your criteria.")
