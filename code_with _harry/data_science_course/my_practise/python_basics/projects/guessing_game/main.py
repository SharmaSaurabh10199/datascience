"""Example 1: Guessing in a Range from 1 to 50
Now consider a smaller range, from 1 to 50, with the same target number 42. Here's how the guesses might proceed:

Guess 1: 25 → Too low
Guess 2: 37 → Too low
Guess 3: 43 → Too high
Guess 4: 40 → Too low
Guess 5: 41 → Too low
Guess 6: 42 → Correct!"""
import random
def guessing_game():
    bottom= int(input("Enter the lower bound"))
    top= int(input("Enter the upper bound"))
    # generate a random no between top and bottom 
    target= random.randint(bottom,top)
    
    iter=0
    while(True):
        iter+=1
        gussed_number= int( input("Guess the number"))
        if(gussed_number>target):
            print("Try again: your guess is too high")
        elif(gussed_number<target):
            print("Try again: your guess is too low")
        else:
            print("Correct")
            print(iter)
            break

guessing_game()