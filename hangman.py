import random as r
from words import words
import string

def valid_word(words):
    w = r.choice(words)
    while (" " or "_" or "-") in w :
            w = r.choice(words)
    return w.upper()

def hangman(word):
  word_letter = set(word)
  alpha = set(string.ascii_uppercase)
  used_letter = set()
  life = 6

  while len(word_letter) >0 and life >0:
    word_list =[]
    print("you have used "," ".join(used_letter)," \nlife remaining : ",life)
    for i in word:
      if i in used_letter:
        word_list.append(i)
      else:
        word_list.append("-")
    print("word : "," ".join(word_list))
    user = input("Guess a letter: ").upper()
    if user in alpha - used_letter:
      used_letter.add(user)
      if user in word_letter:
        word_letter.remove(user)
      else:
        life -= 1
    elif user in used_letter:
      print("You have already used this char try again")
    else:
      print("Invalid char")
  if life == 0:
    print("Sorry You died, the word was ",word)
  else:
    print("Yay you found the word ",word," correctly !!")

word = valid_word(words)
hangman(word)