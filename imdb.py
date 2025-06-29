import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

def scrape_imdb_top_100():
    URL = 'https://www.imdb.com/chart/top/'
    headers = {
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = soup.select('td.titleColumn')
    crew = [a['title'] for a in soup.select('td.titleColumn a')]
    ratings = soup.select('td.imdbRating strong')

    data = []

    for i in range(100):  # Top 100 movies
        movie_title = movies[i].a.text
        movie_year = int(movies[i].span.text.strip('()'))
        movie_rating = float(ratings[i].text)
        movie_director_stars = crew[i]
        movie_link = "https://www.imdb.com" + movies[i].a['href']

        data.append({
            'Title': movie_title,
            'Year': movie_year,
            'Rating': movie_rating,
            'Director and Stars': movie_director_stars,
            'Link': movie_link
        })

    df = pd.DataFrame(data)
    df.to_csv('imdb_top_100.csv', index=False)
    print("✅ Data saved to imdb_top_100.csv")

    return df

def plot_rating_vs_year(df):
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['Rating'], color='crimson', edgecolors='black')
    plt.title('IMDb Top 100 Movies: Rating vs Year', fontsize=16)
    plt.xlabel('Release Year', fontsize=12)
    plt.ylabel('IMDb Rating', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

# --- Run the Script ---
if __name__ == "__main__":
    df = scrape_imdb_top_100()
    plot_rating_vs_year(df)
