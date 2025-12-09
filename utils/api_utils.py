import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def post(path, json_data):
    return requests.post(BASE_URL + path, json=json_data)

def get(path):
    return requests.get(BASE_URL + path)


