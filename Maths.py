import math
while True:
    print("\n1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Power")
    print("6.Square Root")
    print("7.Factorial")
    print("8.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print("Result:", a + b)

    elif choice == "2":
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print("Result:", a - b)

    elif choice == "3":
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print("Result:", a * b)

    elif choice == "4":
        a = float(input("First number: "))
        b = float(input("Second number: "))
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")

    elif choice == "5":
        a = float(input("Base: "))
        b = float(input("Exponent: "))
        print("Result:", a ** b)

    elif choice == "6":
        a = float(input("Enter number: "))
        if a >= 0:
            print("Result:", math.sqrt(a))
        else:
            print("Invalid input")

    elif choice == "7":
        a = int(input("Enter number: "))
        if a >= 0:
            print("Result:", math.factorial(a))
        else:
            print("Invalid input")

    elif choice == "8":
        break

    else:
        print("Invalid choice")