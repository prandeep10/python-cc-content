# Input age and citizenship status from the user
age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ").lower()

# Check if the user meets the voting requirements
if age >= 18 and citizen == "yes":
    print("You are eligible to vote in the election.")
else:
    print("Sorry, you do not meet the voting requirements.")
