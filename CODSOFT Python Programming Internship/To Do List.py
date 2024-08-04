import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        # Task input
        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(root, textvariable=self.task_var, font=('Arial', 14))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add task button
        self.add_button = tk.Button(root, text="Add Task", command=self.add, font=('Arial', 12, 'bold'), bg='blue', fg='white')
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=('Arial', 14, 'bold'), bg='purple', fg='white', width=50, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Update and delete buttons
        self.update_button = tk.Button(root, text="Update Task", command=self.update, font=('Arial', 12, 'bold'), bg='green', fg='white')
        self.update_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete, font=('Arial', 12, 'bold'), bg='red', fg='white')
        self.delete_button.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    def add(self):
        task = self.task_var.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            updated_task = self.task_var.get()
            if updated_task:
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, updated_task)
                self.task_var.set("")
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()
