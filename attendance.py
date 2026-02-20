import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create main application window
root = tk.Tk()
root.title("Attendance Tracker")
root.geometry("600x400")

# Data storage
data = pd.DataFrame(columns=["Name", "Attendance"])

def add_student():
    name = name_entry.get()
    if name:
        global data
        if name not in data["Name"].values:
            data = pd.concat([data, pd.DataFrame([[name, 0]], columns=["Name", "Attendance"])], ignore_index=True)
            update_list()
            name_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Student already exists!")
    else:
        messagebox.showerror("Error", "Enter a valid name!")

def mark_attendance():
    selected = student_listbox.curselection()
    if selected:
        global data
        index = selected[0]
        data.at[index, "Attendance"] += 1
        update_list()
    else:
        messagebox.showerror("Error", "Select a student!")

def update_list():
    student_listbox.delete(0, tk.END)
    for _, row in data.iterrows():
        student_listbox.insert(tk.END, f"{row['Name']} - {row['Attendance']} days")

def show_graph():
    if not data.empty:
        plt.figure(figsize=(8, 5))
        plt.bar(data["Name"], data["Attendance"], color='skyblue')
        plt.xlabel("Students")
        plt.ylabel("Attendance Days")
        plt.title("Attendance Overview")
        plt.xticks(rotation=45)
        plt.show()
    else:
        messagebox.showerror("Error", "No data to display!")

# UI Elements
frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(frame, text="Student Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = ttk.Entry(frame, width=20)
name_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Button(frame, text="Add Student", command=add_student).grid(row=0, column=2, padx=5, pady=5)

student_listbox = tk.Listbox(frame, width=40, height=10)
student_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

ttk.Button(frame, text="Mark Attendance", command=mark_attendance).grid(row=2, column=0, padx=5, pady=5)

ttk.Button(frame, text="Show Graph", command=show_graph).grid(row=2, column=1, padx=5, pady=5)

ttk.Button(frame, text="Exit", command=root.quit).grid(row=2, column=2, padx=5, pady=5)

root.mainloop()
