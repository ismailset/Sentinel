import re
from rich import print

def check_password(p):
    score = 0
    if len(p) >= 12: score += 1
    if re.search(r"[A-Z]", p): score += 1
    if re.search(r"[a-z]", p): score += 1
    if re.search(r"[0-9]", p): score += 1
    if re.search(r"[^A-Za-z0-9]", p): score += 1

    levels = ["Very Weak", "Weak", "Okay", "Strong", "Very Strong"]
    print("Password strength:", levels[min(score, 4)])
