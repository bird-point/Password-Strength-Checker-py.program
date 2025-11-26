import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Check length (minimum 8 characters)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one digit.")
    
    # Check for special characters (e.g., !@#$%^&*()_+-=[]{}|;:,.<>?)
    if re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (e.g., !@#$%^&*).")
    
    # Bonus for longer passwords (12+ characters)
    if len(password) >= 12:
        score += 1
    
    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"
    
    return strength, feedback

# Main script
while True:
    password = input("Enter a password to check: ")
    strength, feedback = check_password_strength(password)
    print(f"Password Strength: {strength}")
    ch=input('Do you want to continue checking(y/n) :').lower()
    if ch=='n':
        break
    if feedback:
        print("Suggestions:")
        for item in feedback:
            print(f"- {item}")
