import random
x= int(input("How many numbers would you like to print?: "))
listone=[]
print("Your random numbers are: ",end="")
for i in range(0,x):
    listone.append(random.randrange(1,11))
    print(str(listone[i])+", ",end="")
