# Initialize a variable to store the sum of positive numbers
total_positive = 0

# Take user input for numbers
while True:
    try:
        num = int(input("Enter a number (or a negative number to stop): "))
        
        # Check if the number is negative to exit the loop
        if num < 0:
            break
        
        # Check if the number is zero to skip it
        if num == 0:
            continue
        
        # Add the positive number to the total
        total_positive += num
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Display the sum of positive numbers
print(f"The sum of positive numbers entered is: {total_positive}")
