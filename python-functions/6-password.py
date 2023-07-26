def validate_password(password):
    # Check for password length
    if len(password) < 8:
        return False
    # Check for uppercase, lowercase, and digit
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    # Check for presence of each requirement
    if not has_uppercase or not has_lowercase or not has_digit:
        return False

    # Check for spaces
    if ' ' in password:
        return False

    # If all checks pass
    return True