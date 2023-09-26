import tkinter as tk
from tkinter import messagebox

def calculate_calories():
    try:
        # Get the input values
        fat_grams = float(fat_grams_entry.get())
        carb_grams = float(carb_grams_entry.get())

        # Check if the input values are negative
        if fat_grams < 0 or carb_grams < 0:
            raise ValueError

        # Calculate the calories
        fat_calories = fat_grams * 3.9
        carb_calories = carb_grams * 4.0

        # Display the results
        fat_calories_label.config(text=f"Calories from fat: {fat_calories:.2f} cal")
        carb_calories_label.config(text=f"Calories from carbs: {carb_calories:.2f} cal")
    except ValueError:
        # Display an error message if the input is invalid
        messagebox.showerror("Invalid input", "Please enter valid positive numbers.")

# Create the main window
root = tk.Tk()
root.title("Nutritionist Helper")

# Create a frame to hold the widgets
frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

# Create labels and entry fields for fat and carb grams
tk.Label(frame, text="Enter fat grams:").grid(row=0, column=0, padx=10, pady=5)
fat_grams_entry = tk.Entry(frame, width=10)
fat_grams_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Enter carb grams:").grid(row=1, column=0, padx=10, pady=5)
carb_grams_entry = tk.Entry(frame, width=10)
carb_grams_entry.grid(row=1, column=1, padx=10, pady=5)

# Create a button to calculate the calories
calculate_button = tk.Button(frame, text="Calculate", command=calculate_calories)
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

# Create labels to display the results
fat_calories_label = tk.Label(frame, text="Calories from fat: 0.0 cal")
fat_calories_label.grid(row=3, column=0, columnspan=2, pady=5)

carb_calories_label = tk.Label(frame, text="Calories from carbs: 0.0 cal")
carb_calories_label.grid(row=4, column=0, columnspan=2, pady=5)

# Run the application
root.mainloop()