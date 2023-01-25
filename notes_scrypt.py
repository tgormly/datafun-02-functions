'''
Tim Gormly
This file is used to write and test code while reading through chapters
'''

from decimal import Decimal


# '''
# 10 students take an exam.  
# They either pass or fail. 
# A pass is represented as 1, a fail is represented as 2
# receive data from user showing pass or fail for each student
# display total number of passes, and failures.
# if passes >= 8, display "bonus for instructor
# '''

# # initialize variables
# passes = 0
# failures = 0

# # iterate 10 times, receiving input from user
# for i in range(10):

#     pass_fail = input(f"Did student #{i+1} pass their exam? Enter 1 for pass, 2 for fail: ")

#     if pass_fail == "1":
#         passes += 1
#     else:
#         failures += 1

# # display results
# print(f"{passes} student(s) passed their exam")
# print(f"{failures} student(s) failed their exam")

# if(passes >= 8):
#     print("This instructor deserves a bonus!")


'''initial decimal things'''

# x = Decimal('1000')

# print(x)

# principal = Decimal('1000')

# print(principal)

# rate = Decimal('0.05')

# print(rate)

# print(principal + rate)


# for i in range(1,110):
#     accumulated_total = principal * (1 + rate) ** i
#     print(f"Year {i:>3}, {accumulated_total:<10.0f}")

'''Self Check Decimal'''

# billBeforeTax = Decimal('37.45')
# taxRate = Decimal('0.0625')

# totalBill = billBeforeTax + (billBeforeTax * taxRate)

# print(type(totalBill)) # checking to see if Python automatically assigns Decimal type to new variable - it does

# print(f"{totalBill:10.2f}")

#textbook simplifies this without variable assignments

'''3.17 measures of central tendency'''

# grades = [85, 93, 45, 89, 85]

# print(sum(grades) / len(grades)) # the sum of all values held in the grades list, divided by the number of values in the grades list (the length or 'len' of the list)

# # import statistics module to use these functions
import statistics

# print(f"using statistics module, mean is {statistics.mean(grades)}")
# print(f"using statistics module, median is {statistics.median(grades)}")
# print(f"using statistics module, mode is {statistics.mode(grades)}")

# values = [47, 95, 88, 73, 88, 84]

# print(values)

# values = sorted(values)

# print(f"values sorted: {values}")

# print(f"using statistics module, mean is {statistics.mean(values):.2f}")
# print(f"using statistics module, median is {statistics.median(values):.0f}")
# print(f"using statistics module, mode is {statistics.mode(values)}")

'''Chapter 3 Exercises'''

# 3.1 (Validating User Input) Modify the script of Fig. 3.3 to validate its inputs. For any  input, if the value entered is other than 1 or 2,

# user_input = ''

# while(user_input not in ['1', '2']):
#     user_input = input("Please enter a 1 or 2")

# print("loop exited")

# a = b = 7

# print('a =', a, '\nb =', b)

# for row in range(10):  
#     for column in range(10):
#         print('<' if row% 2 == 1 else '>', end='')   
#     print()

# for i in range(2):
#     for j in range(7):
#         print("@", end='')
#     print()


# for i in range (6):
#     if i == 0:
#         print(f"{'number':>6} {'square':>7} {'cube':>6}")
#     print(f"{i:>6} {i**2:>7} {i**3:>6}")

# print each number held in "number" one at a time

# number = 1234567

# for i in range(7):
#     print(number % 10)
#     number = number // 10

# factorial problem: 3.13

# while(True):
#     try:
#         factortialChoice = int(input("Enter an integer to find its factorial: "))
#         break
#     except Exception as e:
#         print(e)
#         print()
#         print("Try again with a positive integer")

# total = 1

# print(f" you have chosen {factortialChoice}")

# for i in range(factortialChoice, 1, -1):

#     total *= factortialChoice

#     factortialChoice -= 1

# print(f"{total:,}")

import random

# random.seed(32) # this can be un-commented for debugging

# def roll_dice():
#     '''roll 2d6, return values as a tuple'''
#     die1 = random.randrange(1,7)
#     die2 = random.randrange(1,7)
#     return (die1, die2)

# def display_dice(dice): # a tuple will need to be supplied
#     die1, die2 = dice # this unpacks the tuple into these two values
#     print(f"Player rolled {die1} + {die2} = {sum(dice)}")

# die_values = roll_dice() # this returns a tuple and stores it in die_values
# display_dice(die_values) # die_values that were just generated are now displayed

# selfCheckTuple = ('Sue', [89,94,85])

# name, grades = selfCheckTuple

# print(f"{name} earned the following grades: {grades}")


import math


def cube(x):
    return x ** 3

print(f'the cube of 2 is', cube(2))