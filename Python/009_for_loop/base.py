x = int(input("Please enter the line length: "))
y = input("Type 'h' for horizontal and 'v' for vertical: ")
if (y=="v"):
    for x in range(0,x):
        print("P")
elif(y=="h"):
    for x in range(0,x):
        print("P ",end="")
else:
    print("Please input a valid character")
    