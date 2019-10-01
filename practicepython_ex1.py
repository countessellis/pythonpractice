#!/usr/bin/python

import datetime
currenttime = datetime.datetime.now()
currentyear = currenttime.year
myname = raw_input("What's your name?  ")
myage = input("How old are you?  ")
myhundred = currentyear + 100 - myage

howmany = input("How many copies? ")

for i in range (0,howmany):
  print(myname + " is " + str(myage) + " years old and will be 100 in " + str(myhundred) + ".")
