class ValueTooHighError(Exception):
    def __init__(self, message):
        self.message = message
        # super().__init__(self.message)

try:
    value = int(input("Enter a value (0-100): "))
    if value > 100:
        raise ValueTooHighError("Value exceeds the maximum limit of 100.")
    print(f"Value entered: {value}")
except ValueTooHighError as e:
        print("Error:", e)