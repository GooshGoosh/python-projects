"""
My first GUI application using Tkinter.
"""

import tkinter as tk


root = tk.Tk()

root.title("Address Entry Form")

frm_text_entry = tk.Frame(master=root, relief=tk.SUNKEN, borderwidth=1)
frm_text_entry.pack(padx=3, pady=3)

lbl_first_name = tk.Label(master=frm_text_entry, text="First Name:")
lbl_first_name.grid(row=0, column=0, padx=3, pady=3, sticky="e")

ent_first_name = tk.Entry(master=frm_text_entry, width=40)
ent_first_name.grid(row=0, column=1, padx=3, pady=3)

lbl_last_name = tk.Label(master=frm_text_entry, text="Last Name:")
lbl_last_name.grid(row=1, column=0, padx=3, pady=3, sticky="e")

ent_last_name = tk.Entry(master=frm_text_entry, width=40)
ent_last_name.grid(row=1, column=1, padx=3, pady=3)

lbl_address_line1 = tk.Label(master=frm_text_entry, text="Address Line 1:")
lbl_address_line1.grid(row=2, column=0, padx=3, pady=3, sticky="e")

ent_address_line1 = tk.Entry(master=frm_text_entry, width=40)
ent_address_line1.grid(row=2, column=1, padx=3, pady=3)

lbl_address_line2 = tk.Label(master=frm_text_entry, text="Address Line 2:")
lbl_address_line2.grid(row=3, column=0, padx=3, pady=3, sticky="e")

ent_address_line2 = tk.Entry(master=frm_text_entry, width=40)
ent_address_line2.grid(row=3, column=1, padx=3, pady=3)

lbl_city = tk.Label(master=frm_text_entry, text="City:")
lbl_city.grid(row=4, column=0, padx=3, pady=3, sticky="e")

ent_city = tk.Entry(master=frm_text_entry, width=40)
ent_city.grid(row=4, column=1, padx=3, pady=3)

lbl_state_province = tk.Label(master=frm_text_entry, text="State/Province:")
lbl_state_province.grid(row=5, column=0, padx=3, pady=3, sticky="e")

ent_state_province = tk.Entry(master=frm_text_entry, width=40)
ent_state_province.grid(row=5, column=1, padx=3, pady=3)

lbl_postal_code = tk.Label(master=frm_text_entry, text="Postal Code:")
lbl_postal_code.grid(row=6, column=0, padx=3, pady=3, sticky="e")

ent_postal_code = tk.Entry(master=frm_text_entry, width=40)
ent_postal_code.grid(row=6, column=1, padx=3, pady=3)

lbl_country = tk.Label(master=frm_text_entry, text="Country:")
lbl_country.grid(row=7, column=0, padx=3, pady=3, sticky="e")

ent_postal_code = tk.Entry(master=frm_text_entry, width=40)
ent_postal_code.grid(row=7, column=1, padx=3, pady=3)

frm_buttons = tk.Frame(master=root)
frm_buttons.pack(fill=tk.X, ipadx=3, ipady=3)

btn_submit = tk.Button(master=frm_buttons, text="Submit", relief=tk.RAISED)
btn_submit.pack(padx=3, pady=3, side=tk.RIGHT)

btn_clear = tk.Button(master=frm_buttons, text="Clear", relief=tk.RAISED, borderwidth=1)
btn_clear.pack(padx=3, pady=3, side=tk.RIGHT)


root.mainloop()
