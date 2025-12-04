import random
from time import *
import requests

BASE_SONGS = {
    "Nomu": "https://genius.com/Good-kid-nomu-lyrics",
    "Faster": "https://genius.com/Good-kid-faster-lyrics",
    "Drifting": "https://genius.com/Good-kid-drifting-lyrics"
}

BASE_DESC = {
    "Nomu": "https://en.wikipedia.org/wiki/Nomu_(song)",  
    "Faster": "https://en.wikipedia.org/wiki/Faster_(Good_Kid_song)",
    "Drifting": "https://en.wikipedia.org/wiki/Drifting_(Good_Kid_song)"
}

speling = "bad"

def get_song_link(song):
    return BASE_SONGS.get(song, "no song found lol")

def get_description(song):
    return BASE_DESC.get(song, "no desc found lol")

x = input("whats the song name? ")
print("Lyrics page:", get_song_link(x))
print("Description page:", get_description(x))




