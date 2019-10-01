#!/usr/bin/python

n = input("Please enter a number: ")

print "Divisors: " + str([ m for m in range(1, n) if n % m == 0 ])
