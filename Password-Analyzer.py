import re 
import math
from colorama import Fore, Style, init

init()

common_passwords = ["password", "123456", "qwerty", "admin", "welcome", "letmein"]

def calculate_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"\d", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)


def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in common_passwords:
        return 0, ["This is a very common password. Choose something unique."]
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least of 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    return score, feedback

def strength_label(score):
    if score <= 2:
        return Fore.RED + "Weak" + Style.RESET_ALL
    elif score <= 4:
        return Fore.YELLOW + "Medium" + Style.RESET_ALL
    else:
        return Fore.GREEN + "Strong" + Style.RESET_ALL

print(Fore.CYAN + "=== Password Strength Analyzer ===" + Style.RESET_ALL)
password = input("Enter your Password: ")

score, feedback = check_password_strength(password)
entropy = calculate_entropy(password)
strength = strength_label(score)

print("\mPassword Strength:", strength)
print("Password Entropy:", entropy, "bits")

if feedback:
    print(Fore.RED + "Suggestions:" + Style.RESET_ALL)
    for item in feedback:
        print("-", item)
else:
    print(Fore.GREEN + "Your password is strong!" + Style.RESET_ALL)