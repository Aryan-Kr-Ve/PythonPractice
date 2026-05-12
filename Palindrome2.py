num=[]
#works on string
for i in range(6):
    n=(input("Enter a number: "))
    num.append(n)
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")