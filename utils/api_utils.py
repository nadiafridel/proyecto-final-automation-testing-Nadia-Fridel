import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def post(path, json_data):
    """Hace un POST a la API y devuelve la respuesta"""
    return requests.post(BASE_URL + path, json=json_data)

def get(path):
    return requests.get(BASE_URL + path)


