import random
print("Let's Play Math Game")
print("Print 0 for leaving the game")


while True:
    x=random.randint(1,100)
    x1=random.randint(1,100)

    z=int(input(f"Give Answer of {x} + {x1}\n"))

    if z==(x+x1):
        print("yes ypu are right")
    elif z==0:
        break
    else:
        print("You are wrong, correct answer is",x+x1)




