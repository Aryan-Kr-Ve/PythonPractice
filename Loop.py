"""for Loop Examples"""
for i in range(1, 11):
    print(i)
"""Even"""
for i in range(2, 21, 2):
        print(i)
#odd
for i in range(1, 20, 2):
            print(i)
"""sum of two number"""
total = 0
for i in range(1, 11):
    total += i

    print(total)

    num = int(input("Enter a number: "))

"""Multiplication table"""

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

    """Factorial using for loop"""

    num = int(input("Enter a number: "))
    fact = 1

    for i in range(1, num + 1):
        fact *= i

    print(fact)