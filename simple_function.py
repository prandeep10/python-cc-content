# Define a function to calculate the square of a number
def square(number):
    result = number ** 2
    return result

# Initialize the loop control variable
user_input = ""
























# Run a while loop until 'q' is entered
while user_input.lower() != 'q':
    user_input = input("Enter a number to calculate its square (or 'q' to quit): ")
    
    # Check if the user wants to quit
    if user_input.lower() == 'q':
        print("Goodbye!")
        break
    
    try:
        # Convert user input to a number
        num = float(user_input)
        
        # Calculate and display the square
        result = square(num)
        print(f"The square of {num} is {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number or 'q' to quit.")
