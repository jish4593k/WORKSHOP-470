import tkinter as tk
from tkinter import messagebox
import torch
import os

class ToDoApp:
    def __init__(self):
        self.filepath = "todos.txt"
        self.todos = self.reading()

      
        self.tensor_example = torch.tensor([1, 2, 3])

       
        self.root = tk.Tk()
        self.root.title("ToDo App")

       
        self.new_todo_var = tk.StringVar(value="")

        
        self.todo_listbox = tk.Listbox(self.root)
        self.todo_listbox.pack(pady=10)

        self.new_todo_entry = tk.Entry(self.root, textvariable=self.new_todo_var)
        self.new_todo_entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Todo", command=self.add_todo)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Selected", command=self.remove_todo)
        self.remove_button.pack(pady=5)

       
        for todo in self.todos:
            self.todo_listbox.insert(tk.END, todo)

    def reading(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as file:
                todos = file.readlines()
            return [todo.strip() for todo in todos]
        else:
            return []

    def writing(self):
        with open(self.filepath, "w") as file:
            file.writelines(todo + "\n" for todo in self.todos)

    def add_todo(self):
        new_todo = self.new_todo_var.get()
        if new_todo:
            self.todos.append(new_todo)
            self.writing()
            self.todo_listbox.insert(tk.END, new_todo)
            messagebox.showinfo("Added", f"Added '{new_todo}' to the To-Do list.")
            self.new_todo_var.set("")

    def remove_todo(self):
        selected_index = self.todo_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            removed_todo = self.todos.pop(index)
            self.writing()
            self.todo_listbox.delete(selected_index)
            messagebox.showinfo("Removed", f"Removed '{removed_todo}' from the To-Do list.")

    def run_gui(self):
        self.root.mainloop()

def main():
    todo_app = ToDoApp()
    todo_app.run_gui()

if __name__ == "__main__":
    main()
