import pytest
from utils import api_utils

POSTS = [
    {"title": "Test Post 1", "body": "Contenido 1", "userId": 1},
    {"title": "Test Post 2", "body": "Contenido 2", "userId": 2},
]

@pytest.mark.api
@pytest.mark.parametrize("payload", POSTS)
def test_create_post(payload):
    response = api_utils.post("/posts", payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == payload["title"]

@pytest.mark.api
def test_get_posts():
    response = api_utils.get("/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    
    required_keys = {"userId", "id", "title", "body"}
    for post in data[:3]:  # validamos los primeros 3
        assert required_keys <= set(post.keys())

