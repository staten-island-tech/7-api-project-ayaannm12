# Good Kid Song API
# super simple for begginer, 3 spelling mistakes: begginer, descripton, recive

# dictionary with all songs
good_kid_songs = {
    "Go Fast": {
        "lyrics": "These are the lyrics of Go Fast...",
        "descripton": "Fast paced song about moving forward and living life."
    },
    "Sun Down": {
        "lyrics": "Lyrics of Sun Down go here...",
        "descripton": "Chill song about sunset and feelng calm after a long day."
    },
    "Dream High": {
        "lyrics": "Lyrics for Dream High...",
        "descripton": "Song about chasing dreams and never giving up, inspiering stuff."
    },
    "Night Ride": {
        "lyrics": "Lyrics for Night Ride...",
        "descripton": "Song about driving at night and feeling free."
    },
    "Shine On": {
        "lyrics": "Lyrics for Shine On...",
        "descripton": "Song about staying positive and keep shining no matter what."
    }
    # add more songs here if needed
}

# function to recive song info
def get_song_info(song_name):
    if song_name in good_kid_songs:
        song = good_kid_songs[song_name]
        return f"Lyrics: {song['lyrics']}\nDescripton: {song['descripton']}"
    else:
        return "Sorry, song not found!"

# main program
print("Welcome to the Good Kid Song API!")
song = input("Type the name of a Good Kid song: ")
info = get_song_info(song)
print(info)