import customtkinter as ctk
from tkinter import filedialog
from main import analyze_password 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Password Security Analyzer")
app.geometry("1000x900")

title = ctk.CTkLabel(
    app,
    text="🔐 Password Security Analyzer",
    font=("Poppins", 36, "bold"),
    text_color="white"
)

title.pack(pady=20)
name_entry = ctk.CTkEntry(
    app,
    width=600,
    height=45,
    placeholder_text="Enter Your Name"
)
name_entry.pack(pady=15)

email_entry = ctk.CTkEntry(
    app,
    width=600,
    height=45,
    placeholder_text="Enter Your Email"
)
email_entry.pack(pady=15)

password_entry = ctk.CTkEntry(
    app,
    width=600,
    height=45,
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
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1

    progress.set(score / 5)

    if score <= 2:
        strength_label.configure(text="🔴 Password Strength: Weak")
    elif score <= 4:
        strength_label.configure(text="🟡 Password Strength: Medium")
    else:
        strength_label.configure(text="🟢 Password Strength: Strong")
       
def save_report():

    report = result.get("1.0", "end").strip()

    if report:

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")],
            title="Save Password Report"
        )

        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(report)

analyze_btn = ctk.CTkButton(
    app,
    text="Analyze Password",
    command=analyze_clicked,
    width=240,
    height=45,
    corner_radius=12,
    font=("Poppins", 16,"bold"),
    fg_color="#00B4D8",
    hover_color="#0096C7"
)

analyze_btn.pack(pady=10)

progress = ctk.CTkProgressBar(
    app,
     width=750,
     height=18
)
progress.set(0)
progress.pack(pady=10)

strength_label = ctk.CTkLabel(
    app,
    text="Password Strength: Not Checked",
    font=("Poppins", 16, "bold")
)
strength_label.pack(pady=5)

save_btn = ctk.CTkButton(
    app,
    text="💾 Save Report",
    command=save_report,
    width=240,
    height=45,
    corner_radius=12,
    font=("Poppins", 16,"bold"),
    fg_color="#00B4D8",
    hover_color="#0096C7"
)
save_btn.pack(pady=5)

result_heading = ctk.CTkLabel(
    app,
    text="Analysis Report:",
    font=("Poppins", 18, "bold"),
    text_color="white"
)
result_heading.pack(pady=15, padx=10)

result = ctk.CTkTextbox(
    app,
    width=850,
    height=380,
    font=("Poppins", 15),
)
result.pack(pady=20)
footer = ctk.CTkLabel(
    app,
    text="Developed by Varsha Tewatia | © 2026 All Rights Reserved",
    font=("Poppins", 12),
    text_color="gray"
)
footer.pack(pady=10)

app.mainloop()