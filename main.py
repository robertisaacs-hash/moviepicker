import random
import requests
from bs4 import BeautifulSoup
import urllib3

# Disable SSL warnings for corporate environments
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# crawl IMDB Top 250 and randomly select a movie
URL = 'https://www.imdb.com/chart/top'

def main():
    try:
        # Try with SSL verification first
        response = requests.get(URL, timeout=10)
    except requests.exceptions.SSLError:
        print("SSL verification failed. Trying without SSL verification...")
        try:
            # Fallback: disable SSL verification for corporate networks
            response = requests.get(URL, verify=False, timeout=10)
        except requests.exceptions.RequestException as e:
            print(f"Failed to connect to IMDb: {e}")
            print("Please check your internet connection and try again.")
            return
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to IMDb: {e}")
        print("Please check your internet connection and try again.")
        return

    if response.status_code != 200:
        print(f"Failed to retrieve data from IMDb. Status code: {response.status_code}")
        return

    print("Successfully connected to IMDb! Fetching movie data...")

    soup = BeautifulSoup(response.text, 'html.parser')
    #soup = BeautifulSoup(response.text, 'lxml') # faster

    # print(soup.prettify())

    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    ratingtags = soup.select('td.posterColumn span[name=ir]')

    if not movietags or not inner_movietags or not ratingtags:
        print("Could not find movie data on the page. IMDb may have changed their layout.")
        return

    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1] # last item 
        return year

    try:
        years = [get_year(tag) for tag in movietags]
        actors_list = [tag['title'] for tag in inner_movietags] # access attribute 'title'
        titles = [tag.text for tag in inner_movietags]
        ratings = [float(tag['data-value']) for tag in ratingtags] # access attribute 'data-value'
    except (KeyError, ValueError, AttributeError) as e:
        print(f"Error parsing movie data: {e}")
        print("IMDb may have changed their page structure.")
        return

    n_movies = len(titles)
    print(f"Found {n_movies} movies in the Top 250 list!")
    print("\n" + "="*50)

    while(True):
        idx = random.randrange(0, n_movies)
        
        print(f'{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, Starring: {actors_list[idx]}')

        user_input = input('Do you want another movie (y/[n])? ')
        if user_input != 'y':
            break
    

if __name__ == '__main__':
    main()