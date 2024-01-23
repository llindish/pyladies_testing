import pyladies_project1_testinghomework
import pytest

################
#Task1: create 5 different tests for the behavior of the "evaluate" function.
#Task2: create 2 different tests for the "move" function
#Task3: Answer questions
################


# A set of five tests for the 'evaluate' function from the 1D tic-tac-toe game.
# Each test should assert - check if the output of evaluate is equal to the expected result."

def test_evaluate_draw():
  "This function is a test to check if no winers are declared in case when the board is full and nobody won."
  assert pyladies_project1_testinghomework.evaluate("xxooxoxoxoxoxoxoxoxo") == "!"

def test_evaluate_x_wins():
  "This function is a test to check if 'X' is declares as winner if three x's are present at the start of the board."
  assert pyladies_project1_testinghomework.evaluate("xxx   ") == "x"

def test_evaluate_o_wins():
  "This function is a test to check if 'O' is declares as winner if three o's are present at the end of the board."
  assert pyladies_project1_testinghomework.evaluate("   ooo") == "o"

def test_evaluate_continue_game():
  "This function is a test to check if the game keeps on going while none on the players have won."
  assert pyladies_project1_testinghomework.evaluate("xoxoxo  ") == '-'

def test_evaluate_invalid_gameboard():
  "This function is a test to check if the board is invalid with more than 20 characters, so end of game with no winners should be declared."
  assert pyladies_project1_testinghomework.evaluate("xoxoxoxoxoxoxoxoxoxox") == '!'
  

################
# Two tests for the 'move' function from the 1D tic-tac-toe game.

def test_move_invalid_position():
  "This function tests if the move function correctly handles a case when the given position is out of allowed range."
  initial_board = "                  "
  mark = "o"
  position = 22
  assert pyladies_project1_testinghomework.move(initial_board, mark, position) == "Invalid position."

def test_move_one_round():
  "This function tests if the move function correctly updates the board after accepting one 'x' and one 'o' (one round of moves), and checks if the board still has 18 places left."
  initial_board = "                  "
  mark1 = "x"
  position1 = 0
  board_after_first_move = pyladies_project1_testinghomework.move(initial_board, mark1, position1)
  mark2 = "o"
  position2 = 1
  final_board = pyladies_project1_testinghomework.move(board_after_first_move, mark2, position2)
  assert len(final_board) == 20
  assert final_board.count('x') == 1
  assert final_board.count('o') == 1
  assert final_board.count(' ') == 18

################
#run these tests using command: pytest pyladies_project1_testinghomework_tests.py
  
################
#questions
# 1.What is a Python module and how does it differ from a Python package?
  #A module is a python file that can contain one or multiple functions, variables, classes, comments. 
  #While a package is a combination of multiple relevant modules together, that then can be comfortably imported and used for creating new code.

# 2.What are side effects and give some examples.
  #Side effects are un-wanted actions in the code, like asking input from user, printing out information etc., which you should try to avoid when writing modules.
  #A good example was the homework, when origianlly the code had multiple input fields, which made testing of the module functions fail. 
  #Once the game execution part was moved to another pyhton file, you could import the original game module in the test file and run the tests. 

# 3.What are Exceptions and what to do if third-party code that we use throws them?
  #Exceptions are error warnings that get trigegred because most likely you have done something wrong in your code that will probably make it crash and terminate.
  #For someone else's code that throws exceptions, you could try to use the try/except blocks to catch and handle exceptions.

# 4.Using which keywords can you create, throw and catch your new custom Exception?
  #"raise" command is followed by the name of the exception we want to raise and an optional short description of what went wrong.
  #"assert" statement evaluates the expression that follows it. If the result is not true then it raises the AssertionError exception which is interpreted by pytest as a failing test.
  #"with" statement and the raise function can be used to test that your code raises the expected exception.

# 5.Give examples of some benefits of testing?
  #The main benefit of testing is verifying that what you intented your code to do is actually happening.
  #It can catch problems early and avoid human-errors. 
  #Testing can handle big and complicted codes, where manual testing would take too long.


