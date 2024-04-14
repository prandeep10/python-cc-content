import math

def solve_equation():
    print("\nChoose an equation to solve:")
    print("1. Quadratic Equation (ax^2 + bx + c = 0)")
    print("2. Area of a Circle (A = πr^2)")
    print("3. Pythagorean Theorem (c^2 = a^2 + b^2)")
    print("4. Area of a Triangle (A = 1/2 * base * height)")
    print("5. Solve for x in a Linear Equation (ax + b = 0)")
    print("6. Quit (press 'q')")
    
    choice = input("Enter your choice: ")
    
    if choice.lower() == 'q':
        print("Goodbye!")
        return
    
    try:
        if choice == '1':
            a = float(input("Enter the coefficient 'a': "))
            b = float(input("Enter the coefficient 'b': "))
            c = float(input("Enter the coefficient 'c': "))
            
            discriminant = b**2 - 4*a*c
            if discriminant > 0:
                root1 = (-b + math.sqrt(discriminant)) / (2*a)
                root2 = (-b - math.sqrt(discriminant)) / (2*a)
                print(f"The roots are: {root1} and {root2}")
            elif discriminant == 0:
                root = -b / (2*a)
                print(f"The root is: {root}")
            else:
                real_part = -b / (2*a)
                imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
                root1 = complex(real_part, imaginary_part)
                root2 = complex(real_part, -imaginary_part)
                print(f"The roots are complex: {root1} and {root2}")
        
        elif choice == '2':
            radius = float(input("Enter the radius of the circle: "))
            area = math.pi * radius**2
            print(f"The area of the circle is: {area}")
        
        elif choice == '3':
            a = float(input("Enter the length of side 'a': "))
            b = float(input("Enter the length of side 'b': "))
            c = math.sqrt(a**2 + b**2)
            print(f"The length of the hypotenuse 'c' is: {c}")
        
        elif choice == '4':
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = 0.5 * base * height
            print(f"The area of the triangle is: {area}")
        
        elif choice == '5':
            a = float(input("Enter the coefficient 'a': "))
            b = float(input("Enter the coefficient 'b': "))
            if a == 0:
                if b == 0:
                    print("Infinite solutions.")
                else:
                    print("No solution.")
            else:
                x = -b / a
                print(f"The solution for x is: {x}")
        
        else:
            print("Invalid choice. Please select a valid option.")
    
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")
    
    solve_equation()

# Run the equation solver
solve_equation()
