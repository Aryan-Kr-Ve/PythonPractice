"""Sum of numbers"""
i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print(total)

"""Factorial using while loop"""
num = int(input("Enter a number: "))
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print(fact)

"""Reverse a number"""

num = int(input("Enter a number: "))

while num > 0:
    digit = num % 10
    print(digit, end="")
    num //= 10