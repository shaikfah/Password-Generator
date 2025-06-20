import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for length.")
        return

    use_upper = uppercase_var.get()
    use_lower = lowercase_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Selection Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

app = tk.Tk()
app.title("Password Generator")
app.geometry("400x350")
app.resizable(False, False)

tk.Label(app, text="Password Length:").pack(pady=(10, 0))
length_entry = tk.Entry(app, width=10)
length_entry.insert(0, "12")
length_entry.pack(pady=5)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=False)

tk.Checkbutton(app, text="Include Uppercase Letters", variable=uppercase_var).pack(anchor='w', padx=20)
tk.Checkbutton(app, text="Include Lowercase Letters", variable=lowercase_var).pack(anchor='w', padx=20)
tk.Checkbutton(app, text="Include Digits", variable=digits_var).pack(anchor='w', padx=20)
tk.Checkbutton(app, text="Include Special Characters", variable=special_var).pack(anchor='w', padx=20)

tk.Button(app, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", width=20).pack(pady=10)

tk.Label(app, text="Generated Password:").pack()
password_entry = tk.Entry(app, width=30, justify='center')
password_entry.pack(pady=5)

app.mainloop()
