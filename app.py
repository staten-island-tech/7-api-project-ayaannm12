import random
from time import *
import requests


def getGames(Games):
    response = requests.get(f"https://videogamedb.uk/v3/api-docs/{Games.lower()}")
    if response.status_code != 200:
        print("Error fetching data !!!")
        return None
    
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

Games = getGames("Fortnite")
print(Games)

