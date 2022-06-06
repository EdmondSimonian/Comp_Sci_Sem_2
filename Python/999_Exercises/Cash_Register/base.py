# z=0
# x = int(input("How many items are you purchasing?: "))
# for x in range (0,x):
#     print()
#     e= input("What Item are you buying: ")
#     c = int(input("How much does it cost: "))
#     print("Thank you for purchasing " + e)
#     z = z+c
#     print("_________________________________________")
# print("Your total cost is " + str(z))
# print("Thank you for shopping at Fortnite Freddies Foods!")
il = []
pl = []
x= int(input("How many items would you like to buy: "))
for x in range (0,x):
  e = input("What item are you buying: ")
  c = int(input("How much does it cost: "))
  print("Thank you for purchasing "+ e)
  il.append(e)
  pl.append(c)
  print()
#print(str(sum(pl)))
for x in range (0,x+1):
    print("Item "+str(x+1)+": "+il[x]+"-"+str(pl[x]))
    