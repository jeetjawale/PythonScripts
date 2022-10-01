import random
import math

a, b = map(int, input("Enter the range: ").split())
guess = round(math.log(b - a + 1))

print("You have",  guess,  "guesses only to guess the right number.")

x = random.randint(a, b)
while(guess!=0):
    gue_n = int(input("Guess the number: "))
    if(gue_n == x):
        print("Congratulations! You guess the correct number.")
        break
    elif(gue_n>x):
        print("Too high!")
    elif(gue_n<x):
        print("Too low!")
    
    guess -= 1

if(guess == 0):
    print("Better luck next time!!\n You ran out of guesses")
    print("The number was", x)
