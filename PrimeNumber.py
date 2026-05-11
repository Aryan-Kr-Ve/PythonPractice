num = int(input("Enter a Number\n"))

prime = True

if (num <= 1):
    print("Not a Prime Number")

else:
    # This Loop Checks the number from 2 to n-1
    for i in range(2, num):
        if (num % i == 0):
            prime = False
            break

    if (prime):
        print("Prime Number")
    else:
        print("Not a Prime Number")