import random
from time import *
import requests
import tkinter as tk
from tkinter import simpledialog
import builtins
import threading
import sys


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
                print(f"Title: {selection['title']}")
getgames()



root = tk.Tk()
root.title("Free Games API")
root.geometry("700x400")

output = tk.Text(root, wrap="word")
output.pack(expand=True, fill="both")

def gui_print(*args, **kwargs):
    output.insert(tk.END, " ".join(map(str, args)) + "\n")
    output.see(tk.END)

def gui_input(prompt=""):
    return simpledialog.askstring("Input Needed", prompt)

def run_program():
    output.delete("1.0", tk.END)
    builtins.print = gui_print
    builtins.input = gui_input
    try:
        getgames()
    except Exception as e:
        gui_print("Error:", e)

btn = tk.Button(root, text="Find a Free Game", command=lambda: threading.Thread(target=run_program).start())
btn.pack(pady=10)

root.mainloop()