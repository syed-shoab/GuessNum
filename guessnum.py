import random

n = int(input("Enter range difficulty = "))
num = random.randint(0, n)

attempts = 0

difflevel = input("Enter the Level of Difficulty you want to have:(Hard, Medium, Easy) ")

if difflevel == "Hard":
    attempts = 3
    print(f"You have {attempts} attempts to guess the number ")
elif difflevel == "Medium":
    attempts = 5
    print(f"You have {attempts} attempts to guess the number ")
else:
    attempts = 10
    print(f"You have {attempts} attempts to guess the number ")

input("Press Enter to Start the Game ")

while attempts > 0:
    guess = input("Press 'Q' to Quit || Guess a number between 0 and 100:  ")
    attempts -= 1  

    if(guess == 'Q'):
      print("------------------ GAME OVER ------------------")   
      break

    else:
      guess = int(guess)

      if guess < num:
          print("You're guessing too low!")
      elif guess > num:
          print("You're guessing too high!")
      else:
          print("You guessed it!")
          break

      if attempts > 0:
          print(f"You have {attempts} attempts left.")  
      else:
          print(f"Game over! The number was {num}. \n      Try Again Loser..")  






