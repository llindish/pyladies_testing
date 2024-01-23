import pyladies_project1_testinghomework

##step6: run the code
    
print("Welcome 1-Dimensional Tic-tac-toe game!")

player_mark = str(input("What sign would you like to use: x or o? "))

if player_mark == "x" or "o":
  if player_mark == "x":
    pc_mark = "o"
  else:
    pc_mark = "x"
else:
  print("Invalid mark, choose 'x' or 'o'")
  player_mark = str(input("What sign would you like to use: x or o?"))

pyladies_project1_testinghomework.oneD_tictactoe(player_mark, pc_mark)