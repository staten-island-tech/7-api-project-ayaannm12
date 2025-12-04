# this is my apex legends search thing
# i tried to make it look kinda normal but stil simple

import tkinter as tk

# all apex legends with short info
data = {
    "wraith":{"stats":"fast","story":"lab stuff","playstyle":"rush","reviews":"good"},
    "octane":{"stats":"fast but dum","story":"blew legs","playstyle":"run alot","reviews":"fun"},
    "bloodhound":{"stats":"scanner","story":"wild kid","playstyle":"look for ppl","reviews":"nice"},
    "loba":{"stats":"loot","story":"revenant drama","playstyle":"steal","reviews":"good"},
    "pathfinder":{"stats":"robot","story":"look for maker","playstyle":"zip zip","reviews":"fun"},
    "gibraltar":{"stats":"tank","story":"good guy","playstyle":"shield stuff","reviews":"tanky"},
    "lifeline":{"stats":"heal","story":"help ppl","playstyle":"stay alive","reviews":"team likes"},
    "bangalore":{"stats":"shoot","story":"army stuff","playstyle":"bang bang","reviews":"solid"},
    "rampart":{"stats":"walls","story":"builds","playstyle":"hold spot","reviews":"ok"},
    "horizon":{"stats":"float","story":"space mom","playstyle":"lift ppl","reviews":"strong"},
    "seer":{"stats":"scan","story":"eye guy","playstyle":"track","reviews":"mixed"},
    "fuse":{"stats":"boom","story":"explody guy","playstyle":"nade spam","reviews":"fun"},
    "crypto":{"stats":"drone","story":"hack guy","playstyle":"sit alot","reviews":"eh"},
    "valkyrie":{"stats":"fly","story":"northstar","playstyle":"go up","reviews":"mobile"},
    "revenant":{"stats":"robot demon","story":"killer","playstyle":"push ppl","reviews":"creepy"},
    "ash":{"stats":"sharp","story":"science killer","playstyle":"agro","reviews":"cool"},
    "mad maggie":{"stats":"loud","story":"crazy","playstyle":"rush alot","reviews":"noise"},
    "catalyst":{"stats":"goo","story":"witch vibe","playstyle":"block sight","reviews":"cool"},
    "ballistic":{"stats":"guns","story":"old guy","playstyle":"shoot alot","reviews":"good"},
    "conduit":{"stats":"shields","story":"robot core","playstyle":"team help","reviews":"ok"},
}

def dosearch():
    name = entry.get().lower()
    output.delete("1.0", "end")

    if name in data:
        d = data[name]
        t = ""
        t += "stats: " + d["stats"] + "\n"
        t += "story: " + d["story"] + "\n"
        t += "playstyle: " + d["playstyle"] + "\n"
        t += "reviews: " + d["reviews"] + "\n"
        output.insert("end", t)
    else:
        output.insert("end", "that legend isnt here or u speld it wrong")

win = tk.Tk()
win.title("Apex Search")
win.geometry("300x320")

label = tk.Label(win, text="type legend name:")
label.pack(pady=5)

entry = tk.Entry(win, width=25)
entry.pack()

btn = tk.Button(win, text="search", command=dosearch)
btn.pack(pady=5)

output = tk.Text(win, width=33, height=15)
output.pack(pady=5)

win.mainloop()