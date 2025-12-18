import random
from time import *
import requests


def getgames():
    response = requests.get(f"https://www.freetogame.com/api/games?platform=pc")
    if response.status_code != 200:
        print("Error fetching data!")
        print(response.json)
        return None
    else:
        wg1 =input("what Genre of Free Pc games do you wanna look at ?").lower().strip()
    
    data = response.json()
    for game in data:
        print(game["title"])
games = getgames()