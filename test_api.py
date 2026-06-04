import requests

def test_github_api_status():
    url = "https://api.github.com/repos/Veri-ai/Explore-Shape"
    response = requests.get(url)
    assert response.status_code == 200

def test_github_api_repo_name():
    url = "https://api.github.com/repos/Veri-ai/Explore-Shape"
    response = requests.get(url)
    data = response.json()
    assert data["name"] == "Explore-Shape"

def test_github_api_owner():
    url = "https://api.github.com/repos/Veri-ai/Explore-Shape"
    response = requests.get(url)
    data = response.json()
    assert data["owner"]["login"] == "Veri-ai"
