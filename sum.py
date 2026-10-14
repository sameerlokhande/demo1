def calculate_operations(first_number, second_number):
    results = {
        "Addition": add(first_number, second_number),
        "Subtraction": subtract(first_number, second_number),
        "Multiplication": multiply(first_number, second_number),
        "Division": divide(first_number, second_number)
    }
    return results

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
