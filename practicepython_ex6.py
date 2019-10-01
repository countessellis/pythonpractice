#!/usr/bin/python

word = raw_input("Please enter a string: ")


i = 0
j = len(word)-1

while i <= j:
  if word[i] == word [j]:
    i+=1
    j-=1
    continue
  else:
    print word + " is not a paladrome."
    break
else:
  print word + " is a palaprome."


word2 = raw_input("Please enter another string: ")

rev2 = word2[::-1]
if word2 == rev2:
  print word2 + " is a palaprome."
else:
  print word2 + " is not a palaprome."


