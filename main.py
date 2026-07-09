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
        return "❌ Could not connect to breach database."

    hashes = response.text.splitlines()

    for line in hashes:
        hash_suffix, count = line.split(":")

        if hash_suffix == suffix:
            return f"⚠ WARNING!\nThis password has appeared in {count} data breaches.\nPlease choose a different password."

    return "✅ Good news!\nThis password was NOT found in the breach database."
    
def analyze_password(password, name, email):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    result = ""

    history_file = "password_history.txt"

    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            previous_passwords = file.read().splitlines()
            
        if password_hash in previous_passwords:
            result += "\n⚠ Warning: You have already used this password before."
            result += "Reusing passwords is not recommended.\n"

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

    result += "="*20 + "\n"
    result += f"Password Score: {score}/5\n"
    result += "="*20 + "\n"

    percentage = (score / 5) * 100
    result += f"Password Strength Percentage: {percentage:.0f}%\n"

    breach_result = check_password_breach(password)
    result += breach_result + "\n"

    result += "\nSuggestions to improve your password:"
    if len(password) < 8:
        result += "\n- Use at least 8 characters."
    if not any(char.isupper() for char in password):
        result += "\n- Include at least one uppercase letter."
    if not any(char.islower() for char in password):
        result += "\n- Include at least one lowercase letter."
    if not any(char.isdigit() for char in password):
        result += "\n- Include at least one digit."
    if not any(char in special for char in password):
        result += "\n- Include at least one special character."

    result += "\n"
    if password.lower() in common_passwords:
        result += "Warning: Your password is a commonly used password. Consider changing it to something more unique.\n"
    if name in password.lower() :
        result += "Warning: Your password contains your name. Consider changing it to something more unique.\n"
    if email in password.lower() :
        result += "Warning: Your password contains your email. Consider changing it to something more unique.\n"

    for pattern in keyboard_patterns:
        if pattern in password.lower():
            result += f"Warning: Your password contains a common keyboard pattern '{pattern}'. Consider changing it to something more unique.\n"
            break
    for word in dictionary_words:
        if word in password.lower():
            result += f"Warning: Your password contains a common dictionary word '{word}'. Avoid using dictionary words in your password.\n"
            break
    repeat_found = False
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            repeat_found = True
            break
    if repeat_found:
        result += "Warning: Your password contains repeated characters. Avoid using the same character in your password repeatedly.\n"

    if score == 5:
        strength = "Very Strong Password "
    elif score == 4:
        strength = "Strong Password "
    elif score >= 2:
        strength = "Medium Password "
    else:
        strength = "Weak password "
    result += f"\nOverall Strength: {strength}\n"
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
        result += f"Password Entropy: {entropy:.2f} bits\n"
        if entropy < 40:
            result += "Entropy Level: Low (Weak Password)\n"
        elif entropy < 60:
            result += "Entropy Level: Medium (Moderate Password)\n"
        elif entropy < 80:
            result += "Entropy Level: High (Strong Password)\n"
        else:
            result += "Entropy Level: Excellent (Very Strong Password)\n"
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
        result += f"Estimated Time to Crack: {crack_time}\n"

    result += "\nCyberSecurity tip "
    if score ==5 :
        result += "\nGreat ! Never reuse the same password again "
    elif score >=3:
        result += "\nConsider using a password manager for stronger unique password"
    else:
        result += "\nWeak passwords are vulnerable to brute-force attacks"

    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"  
    symbols = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
    all_charachters = letters+numbers+symbols
    generated_password = "" 
    for _ in range(12):
        generated_password += random.choice(all_charachters)
    result += f"\nGenerated Password: {generated_password}\n"

        # Save password hash if it has not been used before
    if not os.path.exists(history_file):
        with open(history_file, "w") as file:
            file.write(password_hash + "\n")
    else:
        with open(history_file, "r") as file:
            previous_passwords = file.read().splitlines()

        if password_hash not in previous_passwords:
            with open(history_file, "a") as file:
                file.write(password_hash + "\n")

    result += "\nThank you for using the Password Strength Checker!"
    result += "\nDeveloped by Varsha Tewatia"

    return result

    