import re

def check_password_strength(password):
    """
    Check if a password meets the strength requirements.
    Returns a tuple of (boolean, list of failed rules)
    """
    failed_rules = []
    
    # Check length
    if len(password) < 8:
        failed_rules.append("Password must be at least 8 characters long")
    
    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        failed_rules.append("Password must contain at least one uppercase letter")
    
    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        failed_rules.append("Password must contain at least one lowercase letter")
    
    # Check for digits
    if not re.search(r'\d', password):
        failed_rules.append("Password must contain at least one digit")
    
    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        failed_rules.append("Password must contain at least one special character")
    
    # Password is strong if no rules were failed
    is_strong = len(failed_rules) == 0
    
    return is_strong, failed_rules

def main():
    print("Password Strength Checker")
    print("------------------------")
    print("Your password must:")
    print("  • Be at least 8 characters long")
    print("  • Contain uppercase and lowercase letters")
    print("  • Contain at least one digit (0-9)")
    print("  • Contain at least one special character (!, @, #, etc.)")
    print()
    
    while True:
        password = input("Enter a password to check (or 'q' to quit): ")
        
        if password.lower() == 'q':
            break
        
        is_strong, failed_rules = check_password_strength(password)
        
        print("\nPassword Check Results:")
        print("----------------------")
        
        if is_strong:
            print("✅ Password is strong!")
        else:
            print("❌ Password is weak. Please fix the following issues:")
            for rule in failed_rules:
                print(f"  • {rule}")
        print()

if __name__ == "__main__":
    main()