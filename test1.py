

import tkinter as tk

apex_data = {
    "wraith": {
        "stats": "low hp kinda but she fast",
        "story": "she was in a lab and got powers",
        "playstyle": "rush and hide",
        "reviews": "ppl say shes cracked"
    },

    "octane": {
        "stats": "fast but hurts himself",
        "story": "blew up legs and got robo legs",
        "playstyle": "run around like psycho",
        "reviews": "fun but dum"
    },

    "bloodhound": {
        "stats": "scan dude",
        "story": "raised by wild stuff idk",
        "playstyle": "scan then hunt",
        "reviews": "team likes him alot"
    }
}

def search_legend():
    name = entry.get().lower()
    if name in apex_data:
        data = apex_data[name]
        out = ""
        out += "stats: " + data["stats"] + "\n"
        out += "story: " + data["story"] + "\n"
        out += "playstyle: " + data["playstyle"] + "\n"
        out += "reviews: " + data["reviews"] + "\n"
        output.delete("1.0", tk.END)
        output.insert(tk.END, out)
    else:
        output.delete("1.0", tk.END)
        output.insert(tk.END, "bro that legend dont exist or u speld it bad")

win = tk.Tk()
win.title("Apex Search lol")
win.geometry("300x300")

label = tk.Label(win, text="type legend name:")
label.pack()

entry = tk.Entry(win)
entry.pack()

btn = tk.Button(win, text="search", command=search_legend)
btn.pack()

output = tk.Text(win, height=10, width=35)
output.pack()

win.mainloop()