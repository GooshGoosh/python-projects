"""
A simple graphical user-interface (GUI) calculator program made using the
tkinter library available in Python.
"""

import tkinter as tk


COLOR = "black"
BTN_X_PAD = 5
BTN_Y_PAD = 5

# The base, size, and title of the GUI window.
root = tk.Tk()
root.title("Tkinter Calculator")    # Set the title of the window.

# Create the frames for the various pieces of the calculator.
frm_number_display = tk.Frame(master=root, relief=tk.SUNKEN, borderwidth=3,
                              padx=3, pady=3)
lbl_number_input = tk.Label(master=root, text="Enter a number:", relief=tk.SUNKEN, borderwidth=1,
                            padx=3, pady=3)
frm_number_input = tk.Frame(master=root, relief=tk.SUNKEN, borderwidth=2,
                            padx=3, pady=3)
frm_button_grid = tk.Frame(master=root, padx=3, pady=3)

root.columnconfigure(0, weight=1, minsize=200) # Set column width.
root.rowconfigure(0, weight=1, minsize=100)         # Set row height for first row.
root.rowconfigure(1, weight=1, minsize=20)          # Set row height for second row.
root.rowconfigure(2, weight=1, minsize=150)         # Set row height for third row.

frm_number_display.grid(row=0, column=0, sticky="nsew", columnspan=2)
frm_number_input.grid(row=1, column=0, sticky="nsew", columnspan=2)
frm_button_grid.grid(row=2, column=0, sticky="nsew", columnspan=2,)

# Create the label to display the current number input as well as the
# result of the calculation.
frm_number_display.columnconfigure(0, weight=1)
frm_number_display.rowconfigure(0, weight=1)

lbl_display = tk.Label(master=frm_number_display, text="Sample Display",
                       bg="white", fg="black",
                       font=('Times New Roman', 15, 'bold'))
lbl_display.grid(row=0, column=0, sticky="nsew")


# Create the entry for user to input their numbers via text.
lbl_number_input = tk.Label(master=frm_number_input, text="Enter Number: ",
                            font=('Times New Roman', 12), padx=2, pady=2)
ent_number_input = tk.Entry(master=frm_number_input, justify='left', width=34)

lbl_number_input.grid(row=0, column=0)
ent_number_input.grid(row=0, column=1)


# Create the button grid to represent the calculator.
# Use rowspan to stretch some buttons across multiple rows.
frm_button_grid.columnconfigure([0, 1, 2, 3], weight=1, minsize=15)
frm_button_grid.rowconfigure([0, 1, 2, 3, 4], weight=1, minsize=45)

btn_clear = tk.Button(master=frm_button_grid, text="C",
                      relief=tk.RAISED, borderwidth=2,
                      padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)
btn_del = tk.Button(master=frm_button_grid, text="Del",
                      relief=tk.RAISED, borderwidth=2,
                      padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)
btn_divide = tk.Button(master=frm_button_grid, text="/",
                       relief=tk.RAISED, borderwidth=2,
                       padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)
btn_multiply = tk.Button(master=frm_button_grid, text="*",
                         relief=tk.RAISED, borderwidth=2,
                         padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)
btn_subtract = tk.Button(master=frm_button_grid, text="-",
                         relief=tk.RAISED, borderwidth=2,
                         padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)
btn_add = tk.Button(master=frm_button_grid, text="+",
                    relief=tk.RAISED, borderwidth=2,
                    padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)
btn_equal = tk.Button(master=frm_button_grid, text="=",
                      relief=tk.RAISED, borderwidth=2,
                      padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)
btn_decimal = tk.Button(master=frm_button_grid, text=".",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)
btn_0 = tk.Button(master=frm_button_grid, text="0",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)
btn_1 = tk.Button(master=frm_button_grid, text="1",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)
btn_2 = tk.Button(master=frm_button_grid, text="2",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)
btn_3 = tk.Button(master=frm_button_grid, text="3",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)
btn_4 = tk.Button(master=frm_button_grid, text="4",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)
btn_5 = tk.Button(master=frm_button_grid, text="5",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)
btn_6 = tk.Button(master=frm_button_grid, text="6",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)
btn_7 = tk.Button(master=frm_button_grid, text="7",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)
btn_8 = tk.Button(master=frm_button_grid, text="8",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)
btn_9 = tk.Button(master=frm_button_grid, text="9",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR)

# First row of buttons.
btn_clear.grid(row=0, column=0, sticky="nsew")
btn_divide.grid(row=0, column=1, sticky="nsew")
btn_multiply.grid(row=0, column=2, sticky="nsew")
btn_subtract.grid(row=0, column=3, sticky="nsew")

# Second row of buttons.
btn_7.grid(row=1, column=0, sticky="nsew")
btn_8.grid(row=1, column=1, sticky="nsew")
btn_9.grid(row=1, column=2, sticky="nsew")
btn_add.grid(row=1, column=3, sticky="nsew")

# Third row of buttons.
btn_4.grid(row=2, column=0, sticky="nsew")
btn_5.grid(row=2, column=1, sticky="nsew")
btn_6.grid(row=2, column=2, sticky="nsew")
btn_del.grid(row=2, column=3, sticky="nsew")

# Fourth row of buttons.
btn_1.grid(row=3, column=0, sticky="nsew")
btn_2.grid(row=3, column=1, sticky="nsew")
btn_3.grid(row=3, column=2, sticky="nsew")
btn_equal.grid(row=3, column=3, rowspan=2, sticky="nsew")

# Fifth row of buttons.
btn_0.grid(row=4, column=0, columnspan=2, sticky="nsew")
btn_decimal.grid(row=4, column=2, sticky="nsew")

# Spawn the window.
root.mainloop()
