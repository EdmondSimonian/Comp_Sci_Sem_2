x = int(input("Please input a number: "))
y = input("Please input an operation: ")
z = int(input("Please enter a second number: "))
if y == "+":
    print(str(x)+y+str(z)+"="+str(x+z))
elif y == "-":
    print(str(x)+y+str(z)+"="+str(x-z))
elif y == "*":
    print(str(x)+y+str(z)+"="+str(x*z))
elif y == "/":
    print(str(x)+y+str(z)+"="+str(x/z))
else:
    print("you dumbass, that is not a valid operation.")