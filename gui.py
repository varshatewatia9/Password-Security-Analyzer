import customtkinter as ctk
from main import analyze_password 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Password Security Analyzer")
app.geometry("800x720")

title = ctk.CTkLabel(
    app,
    text="🔐 Password Security Analyzer",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)
name_entry = ctk.CTkEntry(
    app,
    width=400,
    placeholder_text="Enter Your Name"
)
name_entry.pack(pady=10)

email_entry = ctk.CTkEntry(
    app,
    width=400,
    placeholder_text="Enter Your Email"
)
email_entry.pack(pady=10)

password_entry = ctk.CTkEntry(
    app,
    width=400,
    placeholder_text="Enter Password",
    show="*"
)
password_entry.pack(pady=15)
show_password = ctk.BooleanVar()

def toggle_password():
    if show_password.get():
        password_entry.configure(show="")
    else:
        password_entry.configure(show="*")

show_checkbox = ctk.CTkCheckBox(
    app,
    text="Show Password",
    variable=show_password,
    command=toggle_password
)

show_checkbox.pack(pady=5)

def analyze_clicked():

    password = password_entry.get()
    name = name_entry.get().lower()
    email = email_entry.get().lower()

    output = analyze_password(password, name, email)

    result.delete("1.0", "end")
    result.insert("1.0", output)

analyze_btn = ctk.CTkButton(
    app,
    text="Analyze Password",
    command=analyze_clicked
)
analyze_btn.pack(pady=10)

result = ctk.CTkTextbox(
    app,
    width=700,
    height=300
)
result.pack(pady=20)

app.mainloop()