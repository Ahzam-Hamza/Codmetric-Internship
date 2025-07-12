import tkinter as tk

# Function to encrypt text
def encrypt_text():
    message = message_entry.get()
    shift_value = shift_entry.get()

    if not message:
        result_label.config(text="Please enter a message.")
        return

    if not shift_value.isdigit():
        result_label.config(text="Shift must be a number.")
        return

    shift = int(shift_value)
    encrypted = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted += new_char
        else:
            encrypted += char  # keep symbols or numbers unchanged

    decrypted = ""

    for char in encrypted:
        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted += new_char
        else:
            decrypted += char

    encrypted_output.config(text="Encrypted: " + encrypted)
    decrypted_output.config(text="Decrypted: " + decrypted)

# Create GUI window
window = tk.Tk()
window.title("Caesar Cipher (Beginner)")
window.geometry("420x350")
window.configure(bg="lightgray")

# Title label
tk.Label(window, text="Caesar Cipher Tool", font=("Arial", 16), bg="lightgray").pack(pady=10)

# Input message
tk.Label(window, text="Enter your message:", bg="lightgray").pack()
message_entry = tk.Entry(window, width=40)
message_entry.pack(pady=5)

# Shift input
tk.Label(window, text="Enter shift number:", bg="lightgray").pack()
shift_entry = tk.Entry(window, width=10)
shift_entry.pack(pady=5)

# Button
tk.Button(window, text="Encrypt and Decrypt", command=encrypt_text, bg="green", fg="white").pack(pady=10)

# Output labels
encrypted_output = tk.Label(window, text="", bg="lightgray", font=("Arial", 11))
encrypted_output.pack(pady=5)

decrypted_output = tk.Label(window, text="", bg="lightgray", font=("Arial", 11))
decrypted_output.pack(pady=5)

# Run the app
window.mainloop()
