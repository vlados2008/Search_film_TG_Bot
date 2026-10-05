import requests
from config import API_OMDB

class APIReqest:
    @staticmethod
    def search(name, type):
        resp = requests.get(f"http://www.omdbapi.com/?apikey={API_OMDB}&s={name}&type={type}")
        films = resp.json()
        return films

    @staticmethod
    def info_film(id):
        resp = requests.get(f'http://www.omdbapi.com/?apikey={API_OMDB}&i={id}&plot=full')
        film_descr = resp.json()
        return film_descr
    