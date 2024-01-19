"""
A simple graphical user-interface (GUI) calculator program made using the
tkinter library available in Python.
"""

import tkinter as tk


COLOR = "black"     # Color for the background highlight
BTN_X_PAD = 5       # X-axis padding for the buttons.
BTN_Y_PAD = 5       # Y-axis padding for the buttons.

operator = ""
num_1 = ""
num_2 = ""
result = ""


def reset_values():
    global operator
    global num_1
    global num_2
    global result

    operator = ""
    num_1 = ""
    num_2 = ""


def update_number_display(num_str):
    lbl_display['text'] = num_str


def perform_calculation():
    match operator:

        case '/':
            if float(num_2) == 0:
                result = "Division by zero is undefined"
                reset_values()
            elif "." in num_1 or "." in num_2:
                result = str(float(num_1) / float(num_2))
                reset_values()
            else:
                result = str(int(num_1) / int(num_2))
                reset_values()

        case '*':
            if "." in num_1 or "." in num_2:
                result = str(float(num_1 ) * float(num_2))
                reset_values()
            else:
                result = str(int(num_1 ) * int(num_2))
                reset_values()

        case '-':
            if "." in num_1 or "." in num_2:
                result = str(float(num_1) - float(num_2))
                reset_values()
            else:
                result = str(int(num_1) - int(num_2))
                reset_values()

        case '+':
            if "." in num_1 or "." in num_2:
                result = str(float(num_1) + float(num_2))
                reset_values()
            else:
                result = str(int(num_1) + int(num_2))
                reset_values()

    result.rstrip('.0')
    update_number_display(result)


def clicked_num(num_str):
    global num_1
    global num_2

    if not operator:
        num_1 += num_str
        update_number_display(num_1)
    else:
        num_2 += num_str
        update_number_display(num_2)


def clicked_clear():
    global num_1
    global num_2

    if not operator:
        num_1 = ""

    else:
        num_2 = ""

    update_number_display("")


def clicked_divide():
    global operator

    operator = "/"
    update_number_display("")


def clicked_multiply():
    global operator

    operator = "*"
    update_number_display("")


def clicked_subtract():
    global operator

    operator = "-"
    update_number_display("")


def clicked_add():
    global operator

    operator = "+"
    update_number_display("")


def clicked_del():
    global num_1
    global num_2

    if not operator:
        if num_1:
            num_1 = num_1[:-1]
            update_number_display(num_1)
        else:
            update_number_display("")
    else:
        if num_2:
            num_2 = num_2[:-1]
            update_number_display(num_2)
        else:
            update_number_display("")


def clicked_decimal():
    global num_1
    global num_2

    if not operator:
        num_1 += "."
        update_number_display(num_1)
    else:
        num_2 += "."
        update_number_display(num_2)


def clicked_equal():
    # If there is no operator, then display num_1.
    if not operator:
        update_number_display(num_1)
    # If num_2 has no value, then display num_2.
    elif not num_2:
        update_number_display(num_2)
    # If there is a value for operator, num_1 and num_2, then calculate.
    else:
        perform_calculation()


# The base, size, and title of the GUI window.
root = tk.Tk()
root.title("Tkinter Calculator")

# Create the frames for the various pieces of the calculator.
frm_number_display = tk.Frame(master=root, relief=tk.SUNKEN, borderwidth=3,
                              padx=3, pady=3)
frm_button_grid = tk.Frame(master=root, padx=3, pady=3)

root.columnconfigure(0, weight=1, minsize=300)      # Set column width.
root.rowconfigure(0, weight=4, minsize=175)         # Set row height for first row.
root.rowconfigure(1, weight=6, minsize=300)         # Set row height for third row.

frm_number_display.grid(row=0, column=0, sticky="nsew")
frm_button_grid.grid(row=1, column=0, sticky="nsew")

# Create the label to display the current number input as well as the
# result of the calculation.
frm_number_display.columnconfigure(0, weight=1)
frm_number_display.rowconfigure(0, weight=1)

lbl_display = tk.Label(master=frm_number_display, text="",
                       bg="white", fg="black",
                       font=('Arial', 15, 'bold'))
lbl_display.grid(row=0, column=0, sticky="nsew")


# Create the buttons and button grid to represent the calculator.
frm_button_grid.columnconfigure([0, 1, 2, 3], weight=1, minsize=75)
frm_button_grid.rowconfigure([0, 1, 2, 3, 4], weight=1, minsize=60)

btn_clear = tk.Button(master=frm_button_grid, text="C",
                      relief=tk.RAISED, borderwidth=2,
                      padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                      command=clicked_clear)

btn_del = tk.Button(master=frm_button_grid, text="Del",
                      relief=tk.RAISED, borderwidth=2,
                      padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                      command=clicked_del)

btn_divide = tk.Button(master=frm_button_grid, text="/",
                       relief=tk.RAISED, borderwidth=2,
                       padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                       command=clicked_divide)

btn_multiply = tk.Button(master=frm_button_grid, text="*",
                         relief=tk.RAISED, borderwidth=2,
                         padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                         command=clicked_multiply)

btn_subtract = tk.Button(master=frm_button_grid, text="-",
                         relief=tk.RAISED, borderwidth=2,
                         padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                         command=clicked_subtract)

btn_add = tk.Button(master=frm_button_grid, text="+",
                    relief=tk.RAISED, borderwidth=2,
                    padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                    command=clicked_add)

btn_equal = tk.Button(master=frm_button_grid, text="=",
                      relief=tk.RAISED, borderwidth=2,
                      padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                      command=clicked_equal)

btn_decimal = tk.Button(master=frm_button_grid, text=".",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                        command=clicked_decimal)

btn_0 = tk.Button(master=frm_button_grid, text="0",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                        command=lambda: clicked_num("0"))

btn_1 = tk.Button(master=frm_button_grid, text="1",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                        command=lambda: clicked_num("1"))

btn_2 = tk.Button(master=frm_button_grid, text="2",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                        command=lambda: clicked_num("2"))

btn_3 = tk.Button(master=frm_button_grid, text="3",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                        command=lambda: clicked_num("3"))

btn_4 = tk.Button(master=frm_button_grid, text="4",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                        command=lambda: clicked_num("4"))

btn_5 = tk.Button(master=frm_button_grid, text="5",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                        command=lambda: clicked_num("5"))

btn_6 = tk.Button(master=frm_button_grid, text="6",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                        command=lambda: clicked_num("6"))

btn_7 = tk.Button(master=frm_button_grid, text="7",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                        command=lambda: clicked_num("7"))

btn_8 = tk.Button(master=frm_button_grid, text="8",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                        command=lambda: clicked_num("8"))

btn_9 = tk.Button(master=frm_button_grid, text="9",
                        relief=tk.RAISED, borderwidth=2,
                        padx=BTN_X_PAD, pady=BTN_Y_PAD, highlightbackground=COLOR,
                        command=lambda: clicked_num("9"))

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
