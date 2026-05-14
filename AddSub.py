while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a + b)

    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a - b)

    elif choice == 3:
        break

    else:
        print("Invalid Choice")