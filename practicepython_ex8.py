#!/usr/bin/python

dict = { "paper": "rock", "rock": "scissors", "scissors": "paper" }

while True:

  player1 = raw_input("Player 1, Rock/Paper/Scissors: ")
  while dict.get(player1,"false") == "false":
    player1 = raw_input("Player 1, please chose a valid choise, Rock/Paper/Scissors: ")
  player2 = raw_input("Player 2, Rock/Paper/Scissors: ")
  while dict.get(player2,"false") == "false":
    player2 = raw_input("Player 2, please chose a valid choise, Rock/Paper/Scissors: ")

  if player1 == player2:
    print "It's a tie!"
  elif dict[player1] == player2:
    print "Player 1 won because " + player1 + " beats " + player2 + "!"
  else:
   print "Player 2 won because " + player2 + " beats " + player1 + "!"

  if raw_input("Would you like to play agains? (y/n)") == "n":
    break

print "Thank you for playing."
  
