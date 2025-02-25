import tkinter as tk
from tkinter import messagebox
import json

# File to store tasks
todo_file = "todo_list.json"

def load_tasks():
    try:
        with open(todo_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks():
    with open(todo_file, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        save_tasks()
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        del tasks[selected_index]
        save_tasks()
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def toggle_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["completed"] = not tasks[selected_index]["completed"]
        save_tasks()
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as complete/incomplete!")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        display_text = task["task"] + (" ✔" if task["completed"] else " ✘")
        task_listbox.insert(tk.END, display_text)

# Load tasks initially
tasks = load_tasks()

# GUI setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

task_label=tk.Label(root, text="Enter").place(x=40,y=8)

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack()

btn_frame = tk.Frame(root)
btn_frame.pack()

add_btn = tk.Button(btn_frame, text="Add", command=add_task)
add_btn.pack(side=tk.LEFT, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete", command=delete_task)
delete_btn.pack(side=tk.LEFT, padx=5)

toggle_btn = tk.Button(btn_frame, text="Mark Done/Undone", command=toggle_task)
toggle_btn.pack(side=tk.LEFT, padx=5)

update_listbox()

root.mainloop()
