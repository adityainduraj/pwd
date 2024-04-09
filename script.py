import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to create the database table if it doesn't exist
def create_table():
    conn = sqlite3.connect('password_manager.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (website TEXT, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

# Function to add a new password entry
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect('password_manager.db')
    c = conn.cursor()
    c.execute("INSERT INTO passwords VALUES (?, ?, ?)", (website, username, password))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Password added successfully!")

# Function to retrieve passwords for a given website
def get_password():
    website = website_entry.get()

    conn = sqlite3.connect('password_manager.db')
    c = conn.cursor()
    c.execute("SELECT * FROM passwords WHERE website=?", (website,))
    results = c.fetchall()
    conn.close()

    if results:
        password_info = ""
        for result in results:
            password_info += f"Username: {result[1]}, Password: {result[2]}\n"
        messagebox.showinfo("Passwords", password_info)
    else:
        messagebox.showerror("Error", "Passwords not found for this website.")

# Create main window
root = tk.Tk()
root.title("Password Manager")

# Create labels
website_label = tk.Label(root, text="Website:")
website_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

username_label = tk.Label(root, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

password_label = tk.Label(root, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

# Create entry fields
website_entry = tk.Entry(root)
website_entry.grid(row=0, column=1, padx=10, pady=5)

username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1, padx=10, pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

# Create buttons
add_button = tk.Button(root, text="Add Password", command=add_password)
add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

retrieve_button = tk.Button(root, text="Retrieve Password", command=get_password)
retrieve_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="we")

# Create database table if it doesn't exist
create_table()

# Run the main event loop
root.mainloop()
