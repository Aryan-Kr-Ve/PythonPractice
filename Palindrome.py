num=[]
num1=int(input("Enter a 1st number:"))
num.append(num1)
num2=int(input("Enter a 2nd number:"))
num.append(num2)
num3=int(input("Enter a 3rd number:"))
num.append(num3)
num4=int(input("Enter a 4th number:"))
num.append(num4)
num5=int(input("Enter a 5th number:"))
num.append(num5)
num6=int(input("Enter a 6th number:"))
num.append(num6)
num2=num.copy()
num2.reverse() #returns non if we do num2=num.reverse()
if num==num2:
    print("Palindrome")
else:
    print("Not a Palindrome")


