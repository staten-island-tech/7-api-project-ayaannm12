from time import *
import requests, random, io, urllib
import tkinter as tk
from tkinter import messagebox


def getgames():
    response = requests.get("https://www.freetogame.com/api/games?platform=pc")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    

    else:
        pi = False
        data = response.json()
        all_genres = {game['genre'].lower() for game in data}

        def search_game():
            genre = genre_entry.get().strip().lower()
            if genre in all_genres:
                matches = [g for g in data if g['genre'].lower() == genre]
                selection = random.choice(matches)
                image_response = requests.get(selection['thumbnail'])
                image_data = image_response.content
                image = Image.open(BytesIO(image_data))
                tk_image = ImageTk.PhotoImage(image)
                result_text.set(f"Title: {selection['title']}\n"
                                f"Thumbnail: {selection['thumbnail']}\n"
                                f"Short Description: {selection['short_description']}\n"
                                f"Game URL: {selection['game_url']}")
                image_label.config(image=tk_image)
                image_label.image = tk_image
            else:
                messagebox.showerror("Error", "Genre not found! Please enter a valid genre.")

        window = tk.Tk()
        window.title("Free PC Games Finder")

        tk.Label(window, text="Welcome to the Free Games API!").pack(pady=10)
        tk.Label(window, text="What genre of games are you looking for? (PC games only)").pack(pady=5)

        genre_entry = tk.Entry(window, width=50)
        genre_entry.pack(pady=10)


        search_button = tk.Button(window, text="Find Game", command=search_game)
        search_button.pack(pady=10)

        result_text = tk.StringVar()
        result_label = tk.Label(window, textvariable=result_text, justify="left")
        result_label.pack(pady=10)

getgames()