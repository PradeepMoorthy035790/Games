#computer will find the number user going to guess

import random

def comp_guess(l,u):
  guess =0
  g = "n"
  guess = random.randint(l,u)
   
  while(g == "n"):
    print(guess)
    feedback = input("Is the No. higher(h) or lower (l) or correct (c)")
    temp = guess
      
    if feedback == "h":  #if the comp guessed no is lower than expected no
      guess = random.randint(temp+1,u)

    if feedback == "l":  #if the comp guessed no is higher than expected no
      guess = random.randint(l,temp-1)

    if feedback == "c":
      g = "y"
  print("Wow I guess it....")

print("Hello User \n In this game the user will give the lower and upper limit and guess a No.\n And the computer will find the No.")
l= int(input("Enter the lower limit : "))
u= int(input("Enter the upper limit : "))
comp_guess(l,u) #calling the function