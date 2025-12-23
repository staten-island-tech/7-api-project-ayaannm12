import random
import requests
import tkinter as tk
from PIL import ImageTk, Image
from io import BytesIO
import threading

def getgames(output, entry):
    response = requests.get("https://www.freetogame.com/api/games?platform=pc")
    if response.status_code != 200:
        output.insert(tk.END, "Error fetching data!\n")
        return

    pi = False
    data = response.json()
    all_genres = {game['genre'].lower() for game in data}

    output.insert(tk.END, "Welcome to the free games API\n")
    output.insert(tk.END, "Hello, what genre of games are you looking for? (PC games only)\n")

    def submit():
        nonlocal pi
        gw = entry.get().strip().lower()  # Get genre input from Entry widget
        entry.delete(0, tk.END)  # Clear the input field after reading the genre

        if gw in all_genres and not pi:
            matches = [g for g in data if g['genre'].lower() == gw]
            selection = random.choice(matches)
            pi = True

            output.insert(tk.END, "Here’s a game that falls under that genre:\n")
            output.insert(tk.END, f"Title: {selection['title']}\n")
            output.insert(tk.END, f"Thumbnail: {selection['thumbnail']}\n")
            output.insert(tk.END, f"Short description: {selection['short_description']}\n")
            output.insert(tk.END, f"Game URL: {selection['game_url']}\n")
        elif not pi:
            output.insert(tk.END, "Invalid genre, try again\n")

    # Trigger the genre search when the button is clicked
    button.config(command=submit)

def launch_with_gui():
    window = tk.Tk()
    window.title("Free Games API Launcher")
    window.geometry("600x400")

    # Create output text widget
    output = tk.Text(window, height=15, width=70)
    output.pack(padx=10, pady=10)

    # Create input entry widget
    entry = tk.Entry(window)
    entry.pack(fill="x", padx=10)

    # Create submit button
    button = tk.Button(window, text="Submit Genre")
    button.pack(pady=5)

    # Run the game-fetching logic in a separate thread to avoid blocking the UI
    threading.Thread(target=lambda: getgames(output, entry)).start()

    window.mainloop()

# Launch the GUI
launch_with_gui()
