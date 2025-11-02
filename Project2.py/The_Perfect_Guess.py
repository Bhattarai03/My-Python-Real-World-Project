import random
n=random.randint(1,100)
a=-1
guess=0
while (a!=n):
    
    a=int(input("Guess a number:"))
    if a>n:
        print("Lower Number Please")
        guess +=1
    else:
        print("Higher Number Please")
        guess +=1
    
print(f"You have guessed the number{n} corrrectly in {guess} attempts")