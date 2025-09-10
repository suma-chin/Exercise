def validate_input(value):
    """Validate that the input is a two-digit number."""
    if not value.isdigit() or not (10 <= int(value) <= 99):
        raise ValueError("Input must be a two-digit number.")

def multiply_two_digits(num1, num2):
    """Multiply two two-digit numbers."""
    return num1 * num2