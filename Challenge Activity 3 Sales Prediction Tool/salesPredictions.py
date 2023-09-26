import tkinter as tk
from tkinter import ttk, messagebox

def calculate_profit():
    try:
        projected_sales = float(sales_entry.get())
        profit_margin = float(profit_margin_entry.get())
        profit = projected_sales * (profit_margin / 100)
        profit_label.config(text=f"Projected Profit: ${profit:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for the projected sales and profit margin.")

# Create the main window
root = tk.Tk()
root.title("Sales Prediction Tool")

# Create and configure the frame
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create the labels, entry fields, and button
sales_label = ttk.Label(frame, text="Enter projected total sales ($):")
sales_label.grid(row=0, column=0, sticky=tk.W, pady=5)

sales_entry = ttk.Entry(frame, width=20)
sales_entry.grid(row=1, column=0, sticky=tk.W, pady=5)

profit_margin_label = ttk.Label(frame, text="Enter profit margin (%):")
profit_margin_label.grid(row=2, column=0, sticky=tk.W, pady=5)

profit_margin_entry = ttk.Entry(frame, width=20)
profit_margin_entry.insert(0, "23")  # Default profit margin
profit_margin_entry.grid(row=3, column=0, sticky=tk.W, pady=5)

calculate_button = ttk.Button(frame, text="Calculate Profit", command=calculate_profit)
calculate_button.grid(row=4, column=0, sticky=tk.W, pady=5)

profit_label = ttk.Label(frame, text="Projected Profit: $")
profit_label.grid(row=5, column=0, sticky=tk.W, pady=5)

# Run the application
root.mainloop()