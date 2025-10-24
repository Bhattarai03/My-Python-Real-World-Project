'''
1 for snake
-1 for water 
0 for gun
'''
import random
computerchoice=random.choice([-1,1,0])
your=(input("Enter your choice:"))
dict={"s":1,"w":-1,"g":0}
reversedict={1:"Snake",-1:"Water",0:"gun"}

you=dict[your]


print(f"You choose {reversedict[you]} \n Commputer choose {reversedict[computerchoice]}")

if(computerchoice==your):
    print("Its a draw")
else:
    # if(computerchoice==-1 and you==1):
    #     print("You win")
    # elif(computerchoice==-1 and you==0):
    #     print("You lose")
    # elif(computerchoice==1 and you==-1):
    #     print("You lose")
    # elif(computerchoice==1 and you==0):
    #     print("You win")
    # elif(computerchoice==0 and you==1):
    #     print("You Lose")
    # elif(computerchoice==0 and you==-1):
    #     print("You win")
    # else:
    #     print("Something went wrong!")

    if((computerchoice - you) == -1 or (computerchoice - you)==2):
        print("you lose")
    else:
        print("You win")