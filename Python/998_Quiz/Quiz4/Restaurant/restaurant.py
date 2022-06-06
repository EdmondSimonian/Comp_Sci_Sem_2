import random
resturant = ["CPK", "KFC", "Sake"]
cpk = ["Pasta", "Pizza", "Salad"]
kfc = ["Tenders", "Nuggets", "Sandwich"]
sake = ["Sushi", "Shrimp", "Seaweed"]

x = input("Please choose a resturant from one of the following, CPK, KFC, Sake: ")
if x == resturant[0]:
    print (cpk)
if x == resturant[1]:
    print (kfc)
if x == resturant[2]:
    print (sake)
    
create if statements and ask fr an input of what menu item they want
also write a line of code for the daily special with ranom.randrange 
and create failsafe elifs for if the user types in a wrong input