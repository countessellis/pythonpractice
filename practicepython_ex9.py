#!/usr/bin/python

import random
random.seed()
rand = random.randint(1,9)
guess = 1

while True:

  num = raw_input("(guess " + str(guess) + ") Guess a number between 1 and 9 (type exit to quit): ")

  if num == "exit":
    print "The number was " + rand + "."
    break
  elif int(num) == rand:
    print "That is correct!  It took you " + str(guess) + " guess(es)."
    break
  elif int(num) < rand:
    print "Your number is too low."
  else:
    print "Your number is too high."

  guess+=1
