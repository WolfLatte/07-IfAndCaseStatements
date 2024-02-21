import math
def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y
###############################################################################
# DONE: 1. (4 pts)
#
#   In this module, we will improve upon the calculator that we built in the
#   Session 5 coding exercises.
#
#   First, you will need to grab the functions that you wrote for each of the
#   four main operations:
#     - add
#     - subtract
#     - multiply
#     - divide
#
#   You can simply copy and paste them into this file at the top (above this
#   _TODO_)
#
#   For this _TODO_, we will be rewriting our main() function.
#
#   First, copy your main() function from Session 5 m3 todo #2 and rename it
#   to if_calc().
#
#   Next, make these modifications
#     1. Add another prompt for the user asking which operation they want to
#        do. Make sure to show the user this key in the prompt.
#           (+) Add
#           (-) Subtract
#           (*) Multiply
#           (/) Division
#        The user should then enter one of the operators to indicate which
#        operation they want to do. Make sure you save this to a variable.
#
#     2. Now, using if statements, check which operator the user put and only
#        do the calculation that the user specified instead of all of them. If
#        the user, put something other than one of the operators, print:
#           "Invalid Operation!"
#
#   Your solution should still function just like it did in Session 5 (except
#   for the changes outlined above)   
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def if_calc():
   print(f"Greetings, kind stranger!")

   numberx = int(input("Please input an interger:"))
   numbery = int(input("Please input a second interger:"))
   user_choice = input("What operation would you like to perform?\n(+) Add\n(-) Subtract\n(*) Multiply\n(/) Division\n")
       
   if user_choice == "+":
      a = add(numberx, numbery)
      print(a)
   
   elif user_choice == "-":
      s = subtract(numberx, numbery)
      print(s)
   
   elif user_choice == "*":
      m = multiply(numberx, numbery)
      print(m)
   
   elif user_choice == "/":
      d = divide(numberx, numbery)
      print(d)

   else:
      print("Invalid Operation!")
      
   

if_calc()



###################################### #########################################
# DONE: 2. (4 pts)
#
#   Now, do the same thing that you did in _TODO_ 1, but this time, use case
#   statements in your solution instead of if statements.
#
#   This time rename your function to case_calc(). Also, you do *not* need to
#   re-copy your operation functions. You can simply use them again.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def case_calc():
   numberx = int(input("Please input an interger:"))
   numbery = int(input("Please input a second interger:"))
   user_choice = input("What operation would you like to perform?\n(+) Add\n(-) Subtract\n(*) Multiply\n(/) Division\n")
   
   match user_choice:
      case "+":
         a = add(numberx, numbery)
         print(a)
      case "-":
         s = subtract(numberx, numbery)
         print(s)
      case "*":
         m = multiply(numberx, numbery)
         print(m)
      case "/":
         d = divide(numberx, numbery)
         print(d)
      case other:
         print("Invalid Operation!")

   print("Goodbye Nerd (because you like math)!")
# I moved the goodbye so it would make sense :D 
case_calc()
   