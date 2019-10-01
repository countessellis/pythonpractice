#!/usr/bin/python

l = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
m = []

for n in l:
  if n < 5:
    m.append(n)

print m

print [ n for n in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if n < 5 ]

i = input("Please enter a number: ")

print [ n for n in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if n < i ]
