import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

def clear_tasks():
    listbox.delete(0, tk.END)

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Info", "Tasks saved to tasks.txt")


gan = tk.Tk()
gan.title("To-Do List")


entry = tk.Entry(gan, font=("Helvetica", 15))
entry.pack(pady=10)


add_button = tk.Button(gan, text="Add Task", font=("Helvetica", 10), command=add_task)
add_button.pack()


listbox = tk.Listbox(gan, font=("Helvetica", 15), selectmode=tk.SINGLE)
listbox.pack(pady=10, fill=tk.BOTH, expand=True)


delete_button = tk.Button(gan, text="Delete Task", font=("Helvetica", 12), command=delete_task)
delete_button.pack()



clear_button = tk.Button(gan, text="Clear All", font=("Helvetica", 12), command=clear_tasks)
clear_button.pack()



save_button = tk.Button(gan, text="Save Tasks", font=("Helvetica", 12), command=save_tasks)
save_button.pack()


try:
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        for task in tasks:
            listbox.insert(tk.END, task.strip())
except FileNotFoundError:
    pass


gan.mainloop()