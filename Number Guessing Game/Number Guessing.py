#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
guess = random.randint(1,100)
level=input("Enter 'h' for hard and 'e' for easy\n").lower()
if level =='h':
  attempt=5
else :
  attempt=10
for i in range(attempt-1,-1,-1):
  c=int(input("Enter a number \n"))
  if i==0:
    print("You LoSe")
    break
  if c==guess :
    print(f"Hooray! You win! Completed with{i} attempts remaining")
    break
  elif c>guess :
    print(f"Too High {i} attempts remaining\n")
  elif c<guess:
    print(f"Too low {i} attempts remaining\n")


     

