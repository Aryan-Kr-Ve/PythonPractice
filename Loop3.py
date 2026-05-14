"""Palindrome"""
num = int(input("Enter a number to check Palindrome: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

"""Prime number check"""


num = int(input("Enter a number to check Prime Number: "))
i = 2
prime = True

while i < num:
    if num % i == 0:
        prime = False
        break
    i += 1

if prime and num > 1:
    print("Prime")
else:
    print("Not Prime")
