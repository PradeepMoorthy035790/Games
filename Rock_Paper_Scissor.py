# This game is about Rock, Paper, Scissor
# here computer will play against you using random function

import random

def rps(ch2):
  choice = ["r","p","s"]
  ch1 = random.choice(choice)
  print("your choice : ",ch2)
  print("Computer choice : ",ch1)

  if (ch1=="r" and ch2=="p") or (ch1=="p" and ch2=="s") or (ch1=="s" and ch2=="r"):
    print("You Win !!!")
  elif (ch1==ch2):
    print("draw")
  else:
    print("Computer Won....")

print("Welcome to Rock Paper And Scissor")
print("Now enter Your choice (r,p,s): ")
ch = input()
rps(ch)