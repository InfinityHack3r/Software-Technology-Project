import tkinter as tk
from tkinter import messagebox
import time

def generate_lap_fields():
    for widget in lap_frame.winfo_children():
        widget.destroy()
    
    try:
        lap_count = int(lap_count_entry.get())

        if lap_count < 1:
            raise ValueError
        
        for i in range(lap_count):
            tk.Label(lap_frame, text=f"Lap {i+1} time:").grid(row=i, column=0, padx=10, pady=5)
            tk.Entry(lap_frame, width=5).grid(row=i, column=1, padx=10, pady=5)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number of laps.")

def update_timer():
    if running:
        elapsed_time = time.time() - start_time
        timer_label.config(text=f"Elapsed time: {elapsed_time:.2f} seconds")
        root.after(100, update_timer)  # Update every 100 ms

def start_timer():
    global start_time, running
    start_time = time.time()
    running = True
    update_timer()

def stop_timer():
    global running
    running = False
    elapsed_time = time.time() - start_time
    timer_label.config(text=f"Elapsed time: {elapsed_time:.2f} seconds")

    # Getting the list of all Entry widgets
    entry_widgets = [widget for widget in lap_frame.winfo_children() if isinstance(widget, tk.Entry)]

    # Finding the next available Entry widget to insert the elapsed time
    for entry in entry_widgets:
        if not entry.get():
            entry.insert(0, f"{elapsed_time:.2f}")
            break

def calculate_lap_times():
    try:
        lap_times = [float(entry.get()) for entry in lap_frame.winfo_children() if isinstance(entry, tk.Entry)]
        
        if not lap_times or any(time <= 0 for time in lap_times):
            raise ValueError

        fastest_lap = min(lap_times)
        slowest_lap = max(lap_times)
        average_lap_time = sum(lap_times) / len(lap_times)
        
        results_label.config(text=f"Fastest Lap: {fastest_lap} secs\nSlowest Lap: {slowest_lap} secs\nAverage Lap Time: {average_lap_time:.2f} secs")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid lap times.")

# Create the main window
root = tk.Tk()
root.title("Lap Timer Tool")

# Create a frame to hold the widgets
frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

# Create a label and entry widget for the number of laps
tk.Label(frame, text="Enter number of laps:").grid(row=0, column=0, padx=10, pady=5)
lap_count_entry = tk.Entry(frame, width=5)
lap_count_entry.grid(row=0, column=1, padx=10, pady=5)

# Timer
timer_label = tk.Label(frame, text="Elapsed time: 0.0 seconds")
timer_label.grid(row=3, column=0, columnspan=2)
start_button = tk.Button(frame, text="Start Timer", command=start_timer)
start_button.grid(row=2, column=0, pady=10)
stop_button = tk.Button(frame, text="Stop Timer", command=stop_timer)
stop_button.grid(row=2, column=1, pady=10)

# Create a button to generate lap time fields
generate_fields_button = tk.Button(frame, text="Generate Fields", command=generate_lap_fields)
generate_fields_button.grid(row=1, column=0, columnspan=2, pady=20)

# Create a frame to hold the dynamically generated lap time fields
lap_frame = tk.Frame(frame)
lap_frame.grid(row=4, column=0, columnspan=2)

# Create a button to calculate lap times
calculate_button = tk.Button(frame, text="Calculate", command=calculate_lap_times)
calculate_button.grid(row=5, column=0, columnspan=2, pady=20)

# Create a Label widget to display the results with a dark background and light text
results_label = tk.Label(frame, text="", bg="dark gray", fg="white", width=50, height=5)
results_label.grid(row=6, column=0, columnspan=2, pady=10)

# Initial settings
running = False
start_time = None

# Run the application
root.mainloop()