def add(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2

def subtract(num1, num2):
    """Returns the difference of two numbers."""
    return num1 - num2

def multiply(num1, num2):
    """Returns the product of two numbers."""
    return num1 * num2

def divide(num1, num2):
    """Returns the quotient of two numbers, or an error message if division by zero."""
    if num2 == 0:
        return "cannot divide by zero"
    return num1 / num2