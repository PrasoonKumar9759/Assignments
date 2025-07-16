class CustomError(Exception):
    """Custom exception for specific error handling."""
    def __init__(self, message):
        super().__init__(message)

# Example usage:
def divide(a, b):
    if b == 0:
        raise CustomError("Division by zero is not allowed.")
    return a / b

try:
    result = divide(10, 0)
except CustomError as e:
    print(f"Caught custom error: {e}")


