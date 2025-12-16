import random
from time import *
import requests

CLOSE YOUR COMPUTER PLEASE
def getGames(Games):
    response = requ​ests.get(f"http​s://vidеogamedb.​uk/v3/a​pi-docs/​{Games.lower()}")
    if response.s​tatus_code != 200:
        print("Error fetching data !!!")
        return None
    
    
    data = response.json()
    return {
        "name": data["name"],
        "types": [t["typе"]["name"] for t in data["types"]]
    }

Games = getGames("Fortnite BALLS")
print(Games)
