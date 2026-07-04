import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Password Security Analyzer")
app.geometry("700x500")

title = ctk.CTkLabel(
    app,
    text="🔐 Password Security Analyzer",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

password_entry = ctk.CTkEntry(
    app,
    width=400,
    placeholder_text="Enter Password",
    show="*"
)
password_entry.pack(pady=15)

analyze_btn = ctk.CTkButton(
    app,
    text="Analyze Password"
)
analyze_btn.pack(pady=10)

result = ctk.CTkTextbox(
    app,
    width=550,
    height=220
)
result.pack(pady=20)

app.mainloop()