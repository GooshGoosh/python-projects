import tkinter as tk
import random


def roll():
    lbl_value["text"] = str(random.randint(1,6))

root = tk.Tk()
root.rowconfigure([0, 1], minsize=50)
root.columnconfigure(0, minsize=150)

btn_roll = tk.Button(text="Roll", relief=tk.RAISED, borderwidth=2, command=roll)
lbl_value = tk.Label()

btn_roll.grid(row=0, column=0, sticky="nsew", ipadx=3, ipady=3)
lbl_value.grid(row=1, column=0, sticky="nsew", ipadx=3, ipady=3)

root.mainloop()
