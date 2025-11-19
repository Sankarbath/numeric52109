import math
###
## simple_package - Module operations.py
## Basic online calculator
###

## (Instructions block text here)

# --- Basic Operations ---
def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract one number from another."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide one number by another."""
    return a / b

# --- Complicated Operations (Task 3) ---
def sine(a):
    """Calculate the sine of a number (in radians)."""
    return math.sin(a)

def logarithm(a):
    """Calculate the natural logarithm (base e) of a number."""
    if a <= 0:
        raise ValueError("Logarithm input must be positive.") 
    return math.log(a)

# --- Calculator Interface (Tasks 1 & 2) ---
def calculator_interface():
    print("Welcome to the calculator. Type 'exit' to quit.")
    
    while True:
        user_input = input("Enter command (e.g., add 5 3) >>> ").strip()
        parts = user_input.split()

        if not parts or parts[0].lower() == 'exit':
            print("Exiting calculator.")
            break

        command = parts[0].lower()
        
        # Define Command Groups
        TWO_ARG_COMMANDS = ['add', 'subtract', 'multiply', 'divide']
        ONE_ARG_COMMANDS = ['sine', 'logarithm'] 
        
        try:
            # --- Parsing Logic and Execution ---
            if command in TWO_ARG_COMMANDS:
                # Check for sufficient arguments
                if len(parts) < 3:
                    raise IndexError("Missing second argument.")
                
                # Parse arguments
                a = float(parts[1])
                b = float(parts[2])
                
                # Execute
                if command == 'add':
                    result = add(a, b)
                elif command == 'subtract':
                    result = subtract(a, b)
                elif command == 'multiply':
                    result = multiply(a, b)
                elif command == 'divide':
                    result = divide(a, b)

            elif command in ONE_ARG_COMMANDS:
                # Check for sufficient arguments
                if len(parts) < 2:
                    raise IndexError("Missing argument.")
                
                # Parse single argument
                a = float(parts[1])
                
                # Execute
                if command == 'sine':
                    result = sine(a)
                elif command == 'logarithm':
                    result = logarithm(a)

            else:
                print(f"Error: Unknown command '{command}'")
                continue

            print(f"Result: {result}")
            
        except (IndexError, ValueError):
            # Handles missing arguments or non-numeric input for ALL commands (Task 2)
            print("Error: Check command format. Usage: 'op X Y' or 'op X'.")
        except ZeroDivisionError:
            # Specific handling for division by zero (Task 2)
            print("Error: Cannot divide by zero.")
        except Exception as e:
            # Catch all other unexpected errors (Task 2)
            print(f"An unexpected error occurred: {e}")

