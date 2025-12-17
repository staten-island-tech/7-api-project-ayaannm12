import random
from time import *
import requests

   

def getgames(games):
    response = requests.get(f"https://www.freetogame.com/api/games?platform=pc/{games.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        print(response.json)
        return None
    
    
    data = response.json()
    return {
        "name": data["name"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

games = getgames("pc")
print(games)
