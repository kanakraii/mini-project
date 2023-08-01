import random
import tkinter as tk
from tkinter import messagebox

def pick_option():
    option_choice = int(entry.get())
    if option_choice == 0:
        root.destroy()
    elif option_choice >= 1 and option_choice <= 4:
        chosen_option = options[option_choice - 2]
        messagebox.showinfo("Chosen Option", f"You chose {chosen_option}!")
        #shuffle
        random.shuffle(options)  
    else:
        #Invalid option 
        messagebox.showwarning("Invalid Option", "Please enter a number from 1 to 4 or 0 to exit.")

def submit_question_options():
    global options
    question = question_entry.get()
    options_text = options_entry.get()
    options = options_text.split(",")
    options = [option.strip() for option in options]
    
    question_label.config(text=f"Question: {question}")
    options_label.config(text="Options:")
  
    entry_label.config(text="Enter a number from 1 to 4 to pick an option (enter 0 to exit):")
    submit_button.config(text="Pick Option", command=pick_option)

root = tk.Tk()
root.title("Automated random decision maker")

question_label = tk.Label(root, text="-Enter your question-")
question_label.grid()

question_entry = tk.Entry(root)
question_entry.grid()

options_label = tk.Label(root, text="-Enter your options seperated by a comma-")
options_label.grid()

options_entry = tk.Entry(root)
options_entry.grid()

submit_button = tk.Button(root, text="Submit", command=submit_question_options)
submit_button.grid()

entry_label = tk.Label(root, text="")
entry_label.grid()

entry = tk.Entry(root)
entry.grid()

result_label = tk.Label(root, text="")
result_label.grid()

options = []

root.mainloop()
