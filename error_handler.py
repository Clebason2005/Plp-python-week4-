# Error handling challenge
def get_number():
    while True:
        try:
            user_input = input("Enter a number: ")
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input! Please enter a valid number.")

try:
    num1 = get_number()
    num2 = get_number()
    
    result = num1 / num2
    print(f"Result of {num1} / {num2} = {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("Calculation attempt finished.")
