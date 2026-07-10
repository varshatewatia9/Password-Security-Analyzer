import customtkinter as ctk
from tkinter import filedialog
from main import analyze_password 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Password Security Analyzer")
app.geometry("1200x1000")

title = ctk.CTkLabel(
    app,
    text="🔐 Password Security Analyzer",
    font=("Poppins",42,"bold"),
    text_color="#4CC9F0"
)
title.pack(pady=20)

main_frame = ctk.CTkFrame(
    app,
    width=760,
    height=500,
    corner_radius=25,
    fg_color="#202235",
    border_width=2,
    border_color="#00E5FF"
)

main_frame.pack(pady=20)
main_frame.pack_propagate(False)

name_entry = ctk.CTkEntry(
    main_frame,
    width=600,
    height=45,
    placeholder_text="👤 Full Name"
)
name_entry.pack(pady=15)

email_entry = ctk.CTkEntry(
    main_frame,
    width=600,
    height=45,
    placeholder_text="📧 Email Address"
)
email_entry.pack(pady=15)

password_entry = ctk.CTkEntry(
    main_frame,
    width=600,
    height=45,
    placeholder_text="🔑 Enter Password",
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
    main_frame,
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
    main_frame,
    text="Analyze Password",
    command=analyze_clicked,
    width=260,
    height=48,
    corner_radius=15,
    font=("Poppins", 16,"bold"),
    fg_color="#0077B6",
    hover_color="#023E8A"
)

analyze_btn.pack(pady=10)

progress = ctk.CTkProgressBar(
    main_frame,
     width=750,
     height=18
)
progress.set(0)
progress.pack(pady=10)

strength_label = ctk.CTkLabel(
    main_frame,
    text="📊 Password Strength: Not Checked",
    font=("Poppins", 16, "bold")
)
strength_label.pack(pady=5)

save_btn = ctk.CTkButton(
    main_frame,
    text="💾 Save Report",
    command=save_report,
    width=260,
    height=48,
    corner_radius=15,
    font=("Poppins", 16,"bold"),
    fg_color="#0077B6",
    hover_color="#023E8A"
)
save_btn.pack(pady=5)

report_frame = ctk.CTkFrame(
    app,
    width=920,
    height=420,
    corner_radius=25,
    fg_color="#202235",
    border_width=2,
    border_color="#00E5FF"
)

report_frame.pack(pady=15)
report_frame.pack_propagate(False)

result_heading = ctk.CTkLabel(
    report_frame,
    text="📋 Analysis Report:",
    font=("Poppins", 18, "bold"),
    text_color="white"
)
result_heading.pack(pady=(15,10))

result = ctk.CTkTextbox(
    report_frame,
    width=850,
    height=280,
    font=("Poppins", 15),
    corner_radius=15,
    border_width=2,
    border_color="#00E5FF",
)
result.pack(pady=10)

footer = ctk.CTkLabel(
    app,
    text="🔒 Developed by Varsha Tewatia • Python • CustomTkinter • 2026",
    font=("Poppins", 12),
    text_color="#8A8A8A"
)
footer.pack(pady=(5,10))

app.mainloop()