import random
from time import *
import requests


def getgames():
    response = requests.get("https://www.freetogame.com/api/games?platform=pc")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    

    else:
        pi = False
        data = response.json()
        all_genres = {game['genre'].lower() for game in data}
        print("welcome to the free games API")
        print("Hello what genre of games are you looking for? (this is pc games only btw)")
        while pi == False:
            gw = input("enter genre here: ").strip().lower()
            if gw in all_genres:
                matches = [g for g in data if g['genre'].lower() == gw]
                selection = random.choices(matches)
                pi = True
                print(f"Heres all games that fall under that genre")
                print(f"Title: {selection["title"]}")









getgames()