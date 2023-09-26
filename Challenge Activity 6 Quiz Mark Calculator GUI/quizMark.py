import tkinter as tk

def calculate_total_mark():
    try:
        # Get marks from the entry fields
        marks = [int(entry.get()) for entry in quiz_entries]

        # Validate that each mark is between 0 and 10
        if all(0 <= mark <= 10 for mark in marks):
            # Calculate the total mark and display it in the result label
            total_mark = sum(marks)
            result_label.config(text=f"The total mark for the ST1 quizzes is: {total_mark}")
        else:
            # Display an error message if any mark is out of the range 0-10
            result_label.config(text="Please enter marks between 0 and 10.")
    except ValueError:
        # Display an error message if the inputs are not valid numbers
        result_label.config(text="Please enter valid numbers for all quiz marks.")

# Create the main window
root = tk.Tk()
root.title("ST1 Quiz Mark Calculator")

# Create a frame to hold the widgets
frame = tk.Frame(root)
frame.pack(pady=0, padx=0)

# Create label and entry widgets for the quiz marks and add them to a list
quiz_entries = []
for i in range(1, 5):
    tk.Label(frame, text=f"Enter quiz {i} Marks (out of 10)").grid(row=i-1, column=0, padx=10, pady=0)
    entry = tk.Entry(frame, width=5)
    entry.grid(row=i-1, column=1, padx=10, pady=5)
    quiz_entries.append(entry)

# Create a button to trigger the calculation
btn = tk.Button(frame, text="Calculate Sum", command=calculate_total_mark)
btn.grid(row=4, column=0, pady=0)

btn_quit = tk.Button(frame, text="Quit", command=root.destroy)
btn_quit.grid(row=4, column=1, pady=0)

result_label = tk.Label(frame, text="", bg="lightgray", fg="black", width=50, height=5)
result_label.grid(row=5, column=0, columnspan=2, pady=0)

# Lock window size
root.resizable(False, False)

# Run the application
root.mainloop()