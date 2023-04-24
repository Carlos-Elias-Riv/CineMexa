import asyncio
from tmdb import route, schema
import requests
# Datos que se obtienen de la API de TMDB: 
# ['adult', 'backdrop_path', 'genre_ids', 'id', 'original_language', 
# 'original_title', 'overview', 'popularity', 'poster_path', 'release_date', 
# 'title', 'video', 'vote_average', 'vote_count']



async def main(movie: str, Ratings: list, Overview: list, Genre: list):
    base = route.Base()
    base.key = "d11ee7fa018448855381b42cdcc78dcf"

    movies = await route.Movie().search(movie)
    
    url = 'https://api.themoviedb.org/3/genre/movie/list'
    params = {'api_key': 'd11ee7fa018448855381b42cdcc78dcf'}
    response = requests.get(url, params=params)
    genres = response.json()['genres']

    # Create a dictionary of genres with genre IDs as keys and genre names as values
    genres_dict = {}
    for genre in genres:
        genres_dict[genre['id']] = genre['name']

    
    #for movie in movies['results']:
    if len(movies['results']) > 0:
        movie = movies['results'][0]
        rating = movie['vote_average']
        overview = movie['overview']
        genre = movie['genre_ids']
        Ratings.append(rating)
        Overview.append(overview)
        if len(genre) > 0: 
            Genre.append(genres_dict[genre[0]])
        else: 
            Genre.append(None)
            #print(f'Rating: {rating}, Overview: {overview}, Genre: {genres_dict[genre[0]]}')

    else: 
        Ratings.append(None)
        Overview.append(None)
        Genre.append(None)
        
import pandas as pd

data = pd.read_csv('/Users/cerivera/Documents/ProyectoCineMexicano/RATINGS/peliculasmexas2016-2021.csv')    

pruebas = data['Film'].to_list()

ratings, overview, genre = [], [], []


for peli in pruebas: 
    asyncio.run(main(peli, ratings, overview, genre))

data['tmdbrating'] = ratings
data['overview'] = overview
data['genre'] = genre

data.to_csv('/Users/cerivera/Documents/ProyectoCineMexicano/RATINGS/peliculasmexascontmdbrating.csv', sep=',', encoding='utf-8', index=False)




