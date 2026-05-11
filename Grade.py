a = int(input("Enter Marks\n"))

if (a > 100 or a < 0):
    print("Invalid Input")

elif (a >= 80):
    print("A")

elif (a >= 75):
    print("B")

elif (a >= 60):
    print("C")

else:
    print("D")