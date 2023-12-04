import requests
import os

MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie/"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

API_TOKEN = os.getenv("TMDB_API_TOKEN")
headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_TOKEN}",
    }

def search_movies_from_tmdb(query_input):
    url = "https://api.themoviedb.org/3/search/movie"
    query = {
        "query": f"{query_input}",
        "language": "en-US"
    }
    response = requests.get(url, headers=headers, params=query)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        return f"The request failed with status code {response.status_code}."


def get_movie_info(movie_id: int):
    url = f"{MOVIE_DB_INFO_URL}{movie_id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return f"The request failed with status code {response.status_code}."


def get_movie_image(image_path):
    url = f"{MOVIE_DB_IMAGE_URL}{image_path}"
    return url
