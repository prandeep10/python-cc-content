# Input age from the user
age = int(input("Enter your age: "))

# Check the age category
if age < 18:
    category = "child"
elif age < 65:
    category = "adult"
else:
    category = "old"

# Display the result
print(f"You are categorized as an {category}.")
