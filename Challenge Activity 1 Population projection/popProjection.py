import tkinter as tk
from tkinter import ttk

# Constants
SECONDS_IN_YEAR = 365 * 24 * 60 * 60

def calculate_population():
    try:
        current_population = float(population_entry.get())
        births_interval = float(births_entry.get())
        deaths_interval = float(deaths_entry.get())
        immigration_interval = float(immigration_entry.get())

        births_per_year = SECONDS_IN_YEAR / births_interval
        deaths_per_year = SECONDS_IN_YEAR / deaths_interval
        immigrants_per_year = SECONDS_IN_YEAR / immigration_interval

        annual_growth = births_per_year - deaths_per_year + immigrants_per_year

        for i in range(1, 6):
            projected_population = current_population + (i * annual_growth)
            population_label[i-1].config(text=f"Year {i}: {int(projected_population)}")

    except ValueError:
        error_label.config(text="Please enter valid numbers for the fields.")

# Create main window
root = tk.Tk()
root.title("Population Projection")

frame = ttk.Frame(root, padding="25")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create labels, entries, and button
instruction_label = ttk.Label(frame, text="Enter current Australian population:")
instruction_label.grid(row=0, column=0, sticky=tk.W, pady=5)

population_entry = ttk.Entry(frame, width=20)
population_entry.insert(0, "25000000")  # Placeholder for current population
population_entry.grid(row=1, column=0, sticky=tk.W, pady=5)

births_label = ttk.Label(frame, text="Births every x seconds:")
births_label.grid(row=2, column=0, sticky=tk.W, pady=5)
births_entry = ttk.Entry(frame, width=20)
births_entry.insert(0, "7")  # Placeholder
births_entry.grid(row=3, column=0, sticky=tk.W, pady=5)

deaths_label = ttk.Label(frame, text="Deaths every x seconds:")
deaths_label.grid(row=4, column=0, sticky=tk.W, pady=5)
deaths_entry = ttk.Entry(frame, width=20)
deaths_entry.insert(0, "13")  # Placeholder
deaths_entry.grid(row=5, column=0, sticky=tk.W, pady=5)

immigration_label = ttk.Label(frame, text="Immigration every x seconds:")
immigration_label.grid(row=6, column=0, sticky=tk.W, pady=5)
immigration_entry = ttk.Entry(frame, width=20)
immigration_entry.insert(0, "45")  # Placeholder
immigration_entry.grid(row=7, column=0, sticky=tk.W, pady=5)

calculate_btn = ttk.Button(frame, text="Calculate", command=calculate_population)
calculate_btn.grid(row=8, column=0, sticky=tk.W, pady=5)

error_label = ttk.Label(frame, text="", foreground="red")
error_label.grid(row=9, column=0, sticky=tk.W, pady=5)

population_label = []
for i in range(5):
    label = ttk.Label(frame, text=f"Year {i+1}: ")
    label.grid(row=i+10, column=0, sticky=tk.W, pady=5)
    population_label.append(label)


# Lock window size
root.minsize(290, 500)
root.maxsize(290, 500)

root.mainloop()
