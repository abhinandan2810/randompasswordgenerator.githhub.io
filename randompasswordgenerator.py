import os
import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a random password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            raise ValueError  # Minimum length validation
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid password length (minimum 4).")
        return
    
    # Characters to choose from (uppercase, lowercase, digits, punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Secure random choice of characters
    random_password = ''.join(random.SystemRandom().choice(characters) for _ in range(length))
    
    # Display the password in the entry box
    password_entry.delete(0, tk.END)
    password_entry.insert(0, random_password)

# Function to copy the generated password to the clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Set up the main application window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x400")  # Set window size
root.resizable(False, False)  # Disable window resizing
root.configure(bg="#2C3E50")  # Dark blue-grey background color

# Header Label
header_label = tk.Label(root, text="Random Password Generator", font=("Helvetica", 16, "bold"), fg="#ECF0F1", bg="#2C3E50")
header_label.pack(pady=20)

# Frame for input and buttons
frame = tk.Frame(root, bg="#34495E", bd=2, relief=tk.GROOVE)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Password length input
length_label = tk.Label(frame, text="Enter password length:", font=("Helvetica", 12), bg="#34495E", fg="#000000")
length_label.pack(pady=10)
length_entry = tk.Entry(frame, font=("Helvetica", 12), justify="center")
length_entry.pack(pady=5)
length_entry.insert(0, "12")  # Default length is 12

# Button to generate password
generate_button = tk.Button(frame, text="Generate Password", command=generate_password, font=("Helvetica", 12), bg="#3498DB", fg="#000000", activebackground="#2980B9")
generate_button.pack(pady=15)

# Entry to display generated password
password_entry = tk.Entry(frame, font=("Helvetica", 12), justify="center", width=30)
password_entry.pack(pady=10)

# Button to copy password to clipboard
copy_button = tk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard, font=("Helvetica", 12), bg="#2ECC71", fg="#000000", activebackground="#27AE60")
copy_button.pack(pady=10)

# Footer label
footer_label = tk.Label(root, text="Developed by Abhinandan | Random Password Generator", font=("Helvetica", 8), fg="#BDC3C7", bg="#2C3E50")
footer_label.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
