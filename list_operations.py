# Initialize an empty list
my_list = []

# Define a while loop
while True:
    # Display a menu of operations
    print("\nList Operations:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Display the list")
    print("4. Quit (press 'q')")
    
    # Ask the user for their choice
    choice = input("Enter your choice: ")
    
    # Check if the user wants to quit
    if choice.lower() == 'q':
        print("Goodbye!")
        break
    
    # Perform the chosen operation
    elif choice == '1':
        item = input("Enter an item to add: ")
        my_list.append(item)
    
    elif choice == '2':
        item = input("Enter an item to remove: ")
        try:
            my_list.remove(item)
        except ValueError:
            print(f"{item} not found in the list.")
    
    elif choice == '3':
        print("Current List:", my_list)
    
    else:
        print("Invalid choice. Please select a valid option.")
