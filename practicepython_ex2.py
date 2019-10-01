#!/usr/bin/python

n = input("Enter a number: ")
if n % 2 == 1:
  print str(n) + " is odd."
else:
  print str(n) + " is even."

if n % 4 == 0:
  print str(n) + " is divisible by 4."

m = input("Enter another number: ")

if n % m == 0:
  print str(n) + " is divisible by " + str(m) + "."
else:
  print str(n) + " is not divisible by " + str(m) + "."
