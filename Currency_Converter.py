import tkinter as tk
from tkinter import ttk


# Set the background color for the window
window = tk.Tk()
window.configure(bg= "#EDDCD2")


# Fix the window size
window.resizable(False, False)


# Set the window title
window.title("Currency Converter")


# Define the window geometry
window.geometry("500x300")


from_currency = tk.StringVar()
to_currency = tk.StringVar()

exchange_rates = {}

def convert_currency():
    from_currency_value = from_currency.get()
    to_currency_value = to_currency.get()
    amount = float(amount_entry.get())

    if from_currency_value == to_currency_value:
        output_label.config(text="Error: Same currency can't be converted")
        output_secondary_label.config(text="")
    else:
        # Perform the conversion using the provided code
        converted_amount = convert_currency_function(from_currency_value, to_currency_value, amount)
        output_label.config(text=f"Converted Amount: {converted_amount}")
        output_secondary_label.config(text="As of 26/03/2024 1:24 am")


def load_exchange_rates():
    with open("exchange_rates.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        line_parts = line.strip().split()
        currency_from = line_parts[0]
        currency_to = line_parts[1]
        exchange_rate = float(line_parts[2])

        if currency_from not in exchange_rates:
            exchange_rates[currency_from] = {}
        exchange_rates[currency_from][currency_to] = exchange_rate

        if currency_to not in exchange_rates:
            exchange_rates[currency_to] = {}
        exchange_rates[currency_to][currency_from] = 1 / exchange_rate

def convert_currency_function(from_currency, to_currency, amount):
    converted_amount = amount * exchange_rates[from_currency][to_currency]
    return round(converted_amount, 2)

load_exchange_rates()

def populate_currencies():
    return list(exchange_rates.keys())

from_currency_label = tk.Label(window, text="From Currency:", bg= "#EDDCD2")
from_currency_label.place(relx=0.05, rely=0.1)

from_currency_menu = ttk.Combobox(window, textvariable=from_currency, values=populate_currencies(), state="readonly", justify="center")
from_currency_menu.place(relx=0.3, rely=0.1)

to_currency_label = tk.Label(window, text="To Currency:", bg= "#EDDCD2")
to_currency_label.place(relx=0.05, rely=0.25)

to_currency_menu = ttk.Combobox(window, textvariable=to_currency, values=populate_currencies(), state="readonly", justify="center")
to_currency_menu.place(relx=0.3, rely=0.25)

amount_label = tk.Label(window, text="Amount:", bg= "#EDDCD2")
amount_label.place(relx=0.05, rely=0.4)

# Add a frame for the amount entry with a border
amount_entry_frame = tk.Frame(window, bg= "#EDDCD2", highlightthickness=1, highlightbackground= "black")
amount_entry_frame.place(relx=0.3, rely=0.4, relwidth=0.3, relheight=0.05)

amount_entry = tk.Entry(amount_entry_frame, highlightthickness=0, borderwidth=0, bg= "#EDDCD2")
amount_entry.place(relx=0, rely=0, relwidth=1, relheight=1)

convert_button = tk.Button(window, text="Convert", command=convert_currency, bg= "#CB997E", fg= "white", activebackground= "#AD8C66", activeforeground= "white", bd=0, highlightthickness=0, relief="flat")
convert_button.place(relx=0.4, rely=0.55)

output_label = tk.Label(window, text="", bg= "#EDDCD2")
output_label.place(relx=0.05, rely=0.75)

output_secondary_label = tk.Label(window, text="", bg= "#EDDCD2")
output_secondary_label.place(relx=0.05, rely=0.82)

# Initialize the currency drop-downs
from_currency_menu.current(0)
to_currency_menu.current(1)

# Add the header
header = ttk.Label(window, text="Currency Converter", borderwidth=2, relief="solid", background="#CB997E", foreground="white", font=("Arial", 18, "bold"))
header.place(relx=0.5, rely=0.05, relwidth=1, anchor="center")

window.mainloop()