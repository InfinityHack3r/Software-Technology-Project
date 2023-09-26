import tkinter as tk
from tkinter import messagebox
import os

def display_info():
    name = name_entry.get()
    address = address_entry.get()
    suburb = suburb_entry.get()
    state = state_entry.get()
    postcode = postcode_entry.get()
    telephone = telephone_entry.get()
    course = course_entry.get()

    info = f"Student Information:\n\n" \
           f"Name: {name}\n" \
           f"Address: {address}\n" \
           f"Suburb: {suburb}\n" \
           f"State: {state}\n" \
           f"Postcode: {postcode}\n" \
           f"Telephone: {telephone}\n" \
           f"Course: {course}"

    messagebox.showinfo("Student Information", info)

    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "student_information.txt")

    with open(file_path, "a") as file:
        file.write(info + "\n\n")

# Create main window
root = tk.Tk()
root.title("Student Information Display Tool")

# Create labels and entries for each piece of information
tk.Label(root, text="Student Name:").grid(row=0, column=0, padx=20, pady=5, sticky=tk.E)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=20, pady=5)

tk.Label(root, text="Address:").grid(row=1, column=0, padx=20, pady=5, sticky=tk.E)
address_entry = tk.Entry(root)
address_entry.grid(row=1, column=1, padx=20, pady=5)

tk.Label(root, text="Suburb:").grid(row=2, column=0, padx=20, pady=5, sticky=tk.E)
suburb_entry = tk.Entry(root)
suburb_entry.grid(row=2, column=1, padx=20, pady=5)

tk.Label(root, text="State:").grid(row=3, column=0, padx=20, pady=5, sticky=tk.E)
state_entry = tk.Entry(root)
state_entry.grid(row=3, column=1, padx=20, pady=5)

tk.Label(root, text="Postcode:").grid(row=4, column=0, padx=20, pady=5, sticky=tk.E)
postcode_entry = tk.Entry(root)
postcode_entry.grid(row=4, column=1, padx=20, pady=5)

tk.Label(root, text="Telephone:").grid(row=5, column=0, padx=20, pady=5, sticky=tk.E)
telephone_entry = tk.Entry(root)
telephone_entry.grid(row=5, column=1, padx=20, pady=5)

tk.Label(root, text="Course:").grid(row=6, column=0, padx=20, pady=5, sticky=tk.E)
course_entry = tk.Entry(root)
course_entry.grid(row=6, column=1, padx=20, pady=5)

# Create a button to submit the information
tk.Button(root, text="Submit", command=display_info).grid(row=7, column=0, columnspan=2, pady=20)


# Lock window size
root.minsize(290, 300)
root.maxsize(290, 300)


# Run the application
root.mainloop()