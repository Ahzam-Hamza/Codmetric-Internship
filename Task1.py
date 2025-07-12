import tkinter as tk
from tkinter import messagebox
import random
import string
import re

# Function to generate the password
def generate_password():
    try:
        length = random.randint(16, 20)  # Random length between 16–20
        use_special = special_option.get()  # Check if user wants special characters

        # Base characters (always included)
        all_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits

        if use_special:
            all_chars += string.punctuation  # Add special characters if selected

        # Start password with at least 1 of each important type
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits)
        ]

        # Add at least one special character if option selected
        if use_special:
            password.append(random.choice(string.punctuation))

        # Fill the rest of the password with random characters
        while len(password) < length:
            password.append(random.choice(all_chars))

        # Shuffle the password so characters are mixed
        random.shuffle(password)

        # Join into one string
        final_password = ''.join(password)

        # Show the password in the box
        password_entry.delete(0, tk.END)
        password_entry.insert(0, final_password)

        # Call the strength check function
        check_strength(final_password)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to copy password to clipboard
def copy_password():
    password = password_entry.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied!")

# Function to check how strong the password is
def check_strength(pw):
    score = 0

    # Simple checks to calculate password score
    if len(pw) >= 12:
        score += 1
    if re.search(r"[A-Z]", pw):
        score += 1
    if re.search(r"[a-z]", pw):
        score += 1
    if re.search(r"[0-9]", pw):
        score += 1
    if re.search(r"[!@#$%^&*()_+]", pw):
        score += 1

    # Update the label based on score
    if score <= 2:
        strength_label.config(text="🔴 Weak Password", fg="red")
    elif score <= 4:
        strength_label.config(text="🟡 Strong Password", fg="orange")
    else:
        strength_label.config(text="🟢 Very Strong Password", fg="green")

# Create the window
window = tk.Tk()
window.title("Simple Password Generator")
window.geometry("400x350")
window.configure(bg="lightgray")

# Heading
tk.Label(window, text="Password Generator", font=("Arial", 16), bg="lightgray").pack(pady=10)

# Info
tk.Label(window, text="Password will be 16–20 characters long", bg="lightgray").pack()
tk.Label(window, text="It will always include A-Z, a-z, and 0–9", bg="lightgray").pack()

# Checkbox for special characters
special_option = tk.BooleanVar()
tk.Checkbutton(window, text="Include Special Characters (!@#$)", variable=special_option, bg="lightgray").pack(pady=10)

# Button to generate password
tk.Button(window, text="Generate Password", command=generate_password, bg="green", fg="white").pack(pady=10)

# Entry box to show the password
password_entry = tk.Entry(window, width=30, font=("Arial", 12), justify="center")
password_entry.pack(pady=5)

# Button to copy password
tk.Button(window, text="Copy Password", command=copy_password, bg="blue", fg="white").pack(pady=10)

# Strength label
strength_label = tk.Label(window, text="Password strength will appear here", bg="lightgray", font=("Arial", 10))
strength_label.pack(pady=5)

# Run the window
window.mainloop()
