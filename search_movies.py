import requests
import os

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_ENDPOINT = os.getenv("TMDB_ENDPOINT")      # https://api.themoviedb.org/3/search/movie?api_key=<<api_key>>

params = {
    "api_key": TMDB_API_KEY,
    "language": "pt-BR",
    "page": 1,
}


def search_movies(query):
    """Retorna uma lista de filmes. E para cada filme: self[0] = título, self[1] == ano, self[2] == descrição,
    self[3] == média de votos, self[4] == imagem"""
    params["query"] = query
    response = requests.get(TMDB_ENDPOINT, params=params)
    data = response.json()
    list_of_movies = [[movie["title"],      # movie["title"] retorna o Título do filme traduzido para a língua específicada em params["language"], assim como a descrição também vem traduzida; movie["original_title"] retorna o Título do filme na língua original.
                       movie["release_date"],
                       movie["overview"],
                       float(movie["vote_average"]),
                       f"https://image.tmdb.org/t/p/w500/{movie['poster_path']}"]
                      for movie in data["results"]]
    return list_of_movies
