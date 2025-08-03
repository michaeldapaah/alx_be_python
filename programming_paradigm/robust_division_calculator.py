def safe_divide(numerator, denominator):
    try:
        # Try to convert both inputs to float
        num = float(numerator)
        den = float(denominator)

        # Try division
        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        # Handles non-numeric input
        return "Error: Please enter numeric values only."
