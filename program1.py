import tkinter as tk

# Initialize the Tkinter window
root = tk.Tk()
root.title("Change Calculator")

# Initialize the change dictionary
change = {10: 4, 20: 3, 50: 5, 100: 2, 200: 3, 500: 6, 1000: 1, 0: 0}

# Function to calculate change
def calculate_change():
    user_input = int(change_entry.get())
    remaining = user_input
    change_given = {}

    for currency in sorted(change.keys(), reverse=True):
        if currency == 0:
            break
        while remaining >= currency and change[currency] > 0:
            remaining -= currency
            change_given[currency] = change_given.get(currency, 0) + 1
            change[currency] -= 1

            if change[currency] == 0:
                change[0] += 1

    if remaining == 0:
        result_label.config(text=f"Your change: {user_input}\nChange given: {change_given}\nYour wallet: {change}")
    else:
        result_label.config(text=f"Sorry, unable to provide exact change. Remaining: {remaining}")

    if change[0] == 7:
        result_label.config(text="Sorry, the change basket has finished")

# GUI components
change_label = tk.Label(root, text="Enter Change You Want to Get:")
change_label.pack()

change_entry = tk.Entry(root)
change_entry.pack()

calculate_button = tk.Button(root, text="Calculate Change", command=calculate_change)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter main loop
root.mainloop()
