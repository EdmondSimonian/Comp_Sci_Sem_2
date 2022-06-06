import random
listone=[]
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        listone.append(l)
        #print(l)
a=0
b=0
f.close()
r = random.randrange(12972)
print(listone[r])
for i in range(6):
    x=input("Please enter your guess: ")
    print("You have made" + (i+1) + "guesses.")
    print()
    if (x==listone[r]):
        print("Correct!")
        b=1
        break
    else:
        for j in listone:
            if x==j:
                a=1
        if a==1:
            print("the guess was valid, but it was wrong")
        else:
            print("the guess was invalid.")
        a=0
if b==0:
    print("You lose. The word was: "+listone[r])




