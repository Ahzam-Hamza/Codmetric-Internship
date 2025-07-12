import tkinter as tk

# Function to check password strength
def check_strength():
    password = password_entry.get()
    score = 0
    suggestion = []

    # Length check
    if len(password) >= 12:
        score += 1
    else:
        suggestion.append("Use at least 12 characters.")

    # Check for uppercase
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if has_upper:
        score += 1
    else:
        suggestion.append("Include uppercase letters (A-Z).")

    # Check for lowercase
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if has_lower:
        score += 1
    else:
        suggestion.append("Include lowercase letters (a-z).")

    # Check for digits
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if has_digit:
        score += 1
    else:
        suggestion.append("Add some numbers (0-9).")

    # Check for special characters
    specials = "!@#$%^&*()_+=-{}[]:;\"'<>,.?/\\|`~"
    has_special = False
    for char in password:
        if char in specials:
            has_special = True
            break
    if has_special:
        score += 1
    else:
        suggestion.append("Add special characters (!@#$ etc).")

    # Show result
    if score <= 2:
        result_label.config(text="🔴 Weak Password", fg="red")
    elif score <= 4:
        result_label.config(text="🟡 Strong Password", fg="orange")
    else:
        result_label.config(text="🟢 Very Strong Password", fg="green")

    # Show suggestions
    if suggestion:
        text = "Suggestions:\n"
        for tip in suggestion:
            text += "- " + tip + "\n"
        suggestion_label.config(text=text.strip())
    else:
        suggestion_label.config(text="✅ Your password is very strong!")

# GUI setup
window = tk.Tk()
window.title("Password Strength Checker (Beginner)")
window.geometry("400x320")
window.configure(bg="lightgray")

tk.Label(window, text="Enter a Password:", font=("Arial", 13), bg="lightgray").pack(pady=10)
password_entry = tk.Entry(window, show="*", width=30, font=("Arial", 12), justify="center")
password_entry.pack(pady=5)

tk.Button(window, text="Check Strength", command=check_strength, bg="blue", fg="white").pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12, "bold"), bg="lightgray")
result_label.pack(pady=5)

suggestion_label = tk.Label(window, text="", font=("Arial", 10), bg="lightgray", justify="center", wraplength=350)
suggestion_label.pack(pady=5)

window.mainloop()
