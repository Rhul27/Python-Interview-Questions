# Suppose, There is an analog Clock having second hand only. User has 3 attempts to stop second hand. 
# User will be awarded with points a/c to following :-
# - If second hand stops at [1,5,9,11] :- 10 points
# - If second hand stops at [4,7,8,10] :- 20 points
# - If second hand stops at [3,2,6,12] :- 30 points
# Also, consider there are three players, declare the winner of the game.
# note :- Imagine second hand stops only at digit of clock. 

from time import sleep
def run():
    attempts = 1
    points = 0
    points_table = {}
    name=input("Enter the name of the player : ")
    while True:
        for i in range(1,13):
            try:
                print(i)
                sleep(0.2)
            except KeyboardInterrupt:
                print(f"Stopped at {i}")
                print("Points are added")
                sleep(1)
                if i in [1,5,9,11]:
                    points+=10
                elif i in [4,7,8,10]:
                    points+=20
                elif i in [3,2,6,12]:
                    points+=30
                attempts+=1
                if attempts==4:
                    print(f"{name} is scored {points}")
                    points_table[name]=points
                    ans=input("Is there any other player(y/n) : ").lower()
                    if ans=='y':
                        name=input("Enter the name of the player : ")
                        attempts=1
                        points=0
                    else:
                        print("Final score :",points_table)
                        return
run()