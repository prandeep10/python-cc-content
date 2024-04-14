import tkinter as tk

def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)

def remove_item():
    selected_item_index = listbox.curselection()
    if selected_item_index:
        listbox.delete(selected_item_index)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create an entry widget for adding items
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a button to add items
add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack()

# Create a listbox to display items
listbox = tk.Listbox(root, width=30)
listbox.pack()

# Create a button to remove selected items
remove_button = tk.Button(root, text="Remove Item", command=remove_item)
remove_button.pack()

# Run the tkinter main loop
root.mainloop()
