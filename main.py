import random 
import hashlib
import requests
import os 
import getpass
import math
import customtkinter as ctk

def check_password_breach(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()

    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    url = "https://api.pwnedpasswords.com/range/" + prefix

    response = requests.get(url)

    if response.status_code != 200:
        print("Could not connect to breach database.")
        return

    hashes = response.text.splitlines()

    for line in hashes:
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            print("\n⚠ WARNING!")
            print(f"This password has appeared in {count} data breaches.")
            print("Please choose a different and more unique password.")
            return

    print("\n✅ Good news!")
    print("This password was NOT found in the breach database.")

print("=== Password Strength Checker v2.1 ===")

name = input("Enter your name: ").lower()
email = input("Enter your email: ").lower()
password = getpass.getpass("Enter your password: ")

password_hash = hashlib.sha256(password.encode()).hexdigest()

history_file = "password_history.txt"

if os.path.exists(history_file):
    with open(history_file, "r") as file:
        previous_passwords = file.read().splitlines()

    if password_hash in previous_passwords:
        print("\n⚠ Warning: You have already used this password before.")
        print("Reusing passwords is not recommended.")

common_passwords = ["password", "123456", "qwerty", "abc123", "letmein", "monkey", "welcome", "111111", "baseball", "iloveyou"]
keyboard_patterns = ["qwerty", "asdfgh", "zxcvbn", "123456","asdfghjkl","1q2w3e4r", "qazwsx", "1qaz2wsx", "qwertyuiop"]
dictionary_words = ["hello","admin", "user", "login", "test", "guest", "root", "master","india","country"]

score = 0

if len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

special = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

if any(char in special for char in password):
    score += 1

print("="*20)
print(f"Password Score: {score}/5")
print("="*20)

percentage = (score / 5) * 100
print(f"Password Strength Percentage: {percentage:.0f}%")

check_password_breach(password)

print("\nSuggestions to improve your password:")
if len(password) < 8:
    print("- Use at least 8 characters.")
if not any(char.isupper() for char in password):
    print("- Include at least one uppercase letter.")
if not any(char.islower() for char in password):
    print("- Include at least one lowercase letter.")
if not any(char.isdigit() for char in password):
    print("- Include at least one digit.")
if not any(char in special for char in password):
    print("- Include at least one special character.")

print()
if password.lower() in common_passwords:
    print("Warning: Your password is a commonly used password. Consider changing it to something more unique.")
if name in password.lower() :
    print("Warning: Your password contains your name. Consider changing it to something more unique.")
if email in password.lower() :
    print("Warning: Your password contains your email. Consider changing it to something more unique.")

for pattern in keyboard_patterns:
    if pattern in password.lower():
        print(f"Warning: Your password contains a common keyboard pattern '{pattern}'. Consider changing it to something more unique.")   
        break
for word in dictionary_words:
    if word in password.lower():
        print(f"Warning: Your password contains a common dictionary word '{word}'. Aviod using dictionary words in your password.")   
        break
repeat_found = False
for i in range(len(password) - 2):
    if password[i] == password[i + 1] == password[i + 2]:
        repeat_found = True
        break
if repeat_found:
     print("Warning: Your password contains repeated characters. Avoid using the same character in your password repeatedly.")

if score == 5:
    strength = "Very Strong Password "
elif score == 4:
    strength = "Strong Password "
elif score >= 2:
    strength = "Medium Password "
else:
    strength = "Weak password "
print(strength)
charset = 0
if any(char.islower() for char in password):
    charset += 26
if any(char.isupper() for char in password):
    charset += 26
if any(char.isdigit() for char in password):
    charset += 10
if any(char in special for char in password):
    charset += len(special)
if charset > 0:
    entropy = len(password) * math.log2(charset)
    print(f"Password Entropy: {entropy:.2f} bits")
    if entropy < 40:
        print("Entropy Level: Low (Weak Password)")
    elif entropy < 60:
        print("Entropy Level: Medium (Moderate Password)")
    elif entropy < 80:
        print("Entropy Level: High (Strong Password)")
    else:
        print("Entropy Level: Excellent (Very Strong Password)")
    if entropy < 28:
        crack_time = "Less than a second"
    elif entropy < 36:
        crack_time = "Few minutes"
    elif entropy < 60:  
        crack_time = "Several days"
    elif entropy < 80:
        crack_time = "Several years"
    else:
        crack_time = "Several centuries"
    print(f"Estimated Time to Crack: {crack_time}")

print("\nCyberSecurity tip ")
if score ==5 :
    print("Great ! Never reuse the same password again ")
elif score >=3:
    print("Consider using a password manager for stronger unique password")
else:
    print("Weak passwords are vulnerable to brute-force attacks")

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"  
symbols = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
all_charachters = letters+numbers+symbols
generated_password = "" 
for _ in range(12):
    generated_password += random.choice(all_charachters)
print("\nGenerated Password:" , generated_password)

save = input("Do you want to save the password report to a file? (yes/no): ")
if save.lower()=="yes":
    file=open("password_report.txt","a")
    file.write("\n=========Password Report=========\n")
    file.write(f"Password : {password}\n")
    file.write(f"Password Score: {score}/5\n")
    file.write(f"Strength : {strength}\n")
    file.write("=================================\n")
    file.close()
    with open(history_file, "a") as file:
        file.write(password_hash + "\n")
    print("\nPassword report saved to password_report.txt")

print("\nThank you for using the Password Strength Checker!")
print("Made by Varsha Tewatia")
