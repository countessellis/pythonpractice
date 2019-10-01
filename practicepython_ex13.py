#!/usr/bin/python


def get_interger(prompt="Please enter a number: "):
  return int(input(prompt))

def det_fib(maxcount):
  a = [ 1 ]
  if maxcount == 1:
    return a
  a.append(1)
  while len(a) < maxcount:
    a.append(a[-1]+a[-2])
  else:
    return a
  

print det_fib(get_interger("How many Fibonnaci numbers would you like? "))
