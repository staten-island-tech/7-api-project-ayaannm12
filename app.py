import random
from time import *
import requests


def getgames(games):
    response = requests.get(f"https://www.freetogame.com/api/games?platform=pc")
    if response.status_code != 200:
        print("Error fetching data!")
        print(response.json)
        return None
    
    
    data = response.json()
    return {
        "title": data["title"],
        "platform": [t["platform"]["title"] for t in data["platform"]]
    }

games = getgames("Overwatch 2")
print(games)