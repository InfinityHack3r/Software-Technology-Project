import tkinter as tk
from tkinter import ttk

def convert_to_kg():
    try:
        pounds = float(pound_entry.get())
        kilograms = pounds * 0.454
        result_label.config(text=f"Mass in kilograms: {kilograms:.2f} kg")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Pound to Kilogram Converter")

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create labels, entry field, and button
instruction_label = ttk.Label(frame, text="Enter mass in pounds:")
instruction_label.grid(row=0, column=0, sticky=tk.W, pady=5)

pound_entry = ttk.Entry(frame, width=20)
pound_entry.grid(row=1, column=0, sticky=tk.W, pady=5)

convert_btn = ttk.Button(frame, text="Convert", command=convert_to_kg)
convert_btn.grid(row=2, column=0, sticky=tk.W, pady=5)

result_label = ttk.Label(frame, text="")
result_label.grid(row=3, column=0, sticky=tk.W, pady=5)

# Lock window size
root.minsize(250, 150)
root.maxsize(250, 150)

root.mainloop()