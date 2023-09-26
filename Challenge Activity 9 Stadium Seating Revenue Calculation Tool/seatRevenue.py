import tkinter as tk
from tkinter import messagebox

def calculate_revenue():
    try:
        # Get the input values
        class_a_tickets = int(class_a_entry.get())
        class_b_tickets = int(class_b_entry.get())
        class_c_tickets = int(class_c_entry.get())

        class_a_cost = float(class_a_cost_entry.get())
        class_b_cost = float(class_b_cost_entry.get())
        class_c_cost = float(class_c_cost_entry.get())

        # Check if the input values are negative
        if class_a_tickets < 0 or class_b_tickets < 0 or class_c_tickets < 0 or class_a_cost < 0 or class_b_cost < 0 or class_c_cost < 0:
            raise ValueError

        # Calculate the revenue
        class_a_revenue = class_a_tickets * class_a_cost
        class_b_revenue = class_b_tickets * class_b_cost
        class_c_revenue = class_c_tickets * class_c_cost

        total_revenue = class_a_revenue + class_b_revenue + class_c_revenue

        # Display the total revenue
        revenue_label.config(text=f"Total Revenue: ${total_revenue:.2f}")
    except ValueError:
        # Display an error message if the input is invalid
        messagebox.showerror("Invalid input", "Please enter valid positive numbers.")

# Create the main window
root = tk.Tk()
root.title("Stadium Seating Revenue Calculation Tool")

# Create a frame to hold the widgets
frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

# Create labels and entry fields for each class of seats
tk.Label(frame, text="Class A tickets sold:").grid(row=0, column=0, padx=10, pady=5)
class_a_entry = tk.Entry(frame, width=10)
class_a_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Class B tickets sold:").grid(row=1, column=0, padx=10, pady=5)
class_b_entry = tk.Entry(frame, width=10)
class_b_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Class C tickets sold:").grid(row=2, column=0, padx=10, pady=5)
class_c_entry = tk.Entry(frame, width=10)
class_c_entry.grid(row=2, column=1, padx=10, pady=5)

# Create labels and entry fields for the cost of each class of seats
tk.Label(frame, text="Class A seat cost:").grid(row=0, column=2, padx=10, pady=5)
class_a_cost_entry = tk.Entry(frame, width=10)
class_a_cost_entry.grid(row=0, column=3, padx=10, pady=5)
class_a_cost_entry.insert(0, "20")

tk.Label(frame, text="Class B seat cost:").grid(row=1, column=2, padx=10, pady=5)
class_b_cost_entry = tk.Entry(frame, width=10)
class_b_cost_entry.grid(row=1, column=3, padx=10, pady=5)
class_b_cost_entry.insert(0, "15")

tk.Label(frame, text="Class C seat cost:").grid(row=2, column=2, padx=10, pady=5)
class_c_cost_entry = tk.Entry(frame, width=10)
class_c_cost_entry.grid(row=2, column=3, padx=10, pady=5)
class_c_cost_entry.insert(0, "10")

# Create a button to calculate the revenue
calculate_button = tk.Button(frame, text="Calculate Revenue", command=calculate_revenue)
calculate_button.grid(row=3, column=0, columnspan=4, pady=20)

# Create a label to display the total revenue
revenue_label = tk.Label(frame, text="Total Revenue: $0.00")
revenue_label.grid(row=4, column=0, columnspan=4, pady=5)

# Run the application
root.mainloop()
