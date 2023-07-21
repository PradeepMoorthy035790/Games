#this is a guessing game where the compiler will generate a random no. and u have to guess
# when u give a no it will say "High" or "Low" based on the difference between the random no. and ur no.
# all the no generated will be a whole no

import random

print("WELCOME TO THE GUESSING GAME: ")
print("Enter the limit both lower and upper limit ")

c="y"
while(c == "y"):

  l = int(input("Enter the lower limit: "))
  u = int(input("Enter the upper limit: "))

  r = random.randint(l,u)

  print("You will be given 5 chance to guess the no.")
  print("Here we go.......")
  v = int(input("Enter your guess: "))
  flag = 0
  for i in range(4):
    if v == r:
      print("Hell yeah you got it correct ")
      flag = 1
      break
    else:
      if v-r < 0:
        print("Higher")
      else:
        print("Lower")
      v = int(input("Enter the no. again: "))

  if flag == 1:
    print("Yoo man good guess. Do you want to try again? (y/n)")
    c = input()
  else:
    print("Yoo sorry man you didn't make it ")
    print("Do you want to give it a second try ??(y/n)")
    c = input()
