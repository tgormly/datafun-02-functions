"""
Tim Gormly
1/24/2023
44-608 Data Analytics Fundamentals
Module 2


In this script, there are a few custom functions:

-get_total_goals_scored
    receives a list of integers, and returns a single value equal to the total of all integers contained in the list

-calculate_accuracy
    receives two integer arguments; one representing total shots, and one representing total goals
    returns a float value equal to goals divided by shots

"""

import math
import random

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?
    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = length * width # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)
def get_total_goals_scored(list_of_goals):
    '''
    Return the total number of goals scored by a hockey player.  
    Method receives a list where each entry in the list represents the number of goals scored by the player in one game.  
    Method returns an int value equal to the total number of goals scored
    '''


    # attempt to sum the values in the list
    try:
        # if the list is empty, return 0
        if(len(list_of_goals) == 0):
            return 0
        else:
            return math.fsum(list_of_goals)
    except Exception as e:
        print(f"ERROR: {e}")
        return None

def calculate_accuracy(goals, shots):
    """
    Return a float value equal to goals / shots, to show the players scoring % on their attempted shots
    a return value of 1 represents 100% accuracy - every shot by the player has resulted in a goal
    """
    try:
        accuracy = float(goals / shots)

        if(accuracy >= 1):
            print("The player scored more goals than they shot the puck!  Amazing!")

        return accuracy
    except ZeroDivisionError as e:
        print("ERROR: Cannot divide by zero")
        return None
    except Exception as e:
        print(f"ERROR: {e}")
        return None

def merch_plus_tax(unit_price, tax_rate):
    """
    This method calculates the total cost of a piece of merchandise after sales tax has been added to the cost
    The first parameter, unit_price represents the price of the item without tax
    The second parameter, tax_rate represents the tax multiplier assessed against the item
    """
    try:
        return unit_price + (unit_price * tax_rate)
    except Exception as e:
        print(f"ERROR: {e}")
        return None


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Explore some functions in the math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print()
    print(f"math.comb(5,3) = {math.comb(5,3)}")
    print(f"math.perm(5,3) = {math.perm(5,3)}")
    print()
    print(f"math.pi = {math.pi}")
    print()
    print(f"math.degrees(2 * math.pi) = {math.degrees(2 * math.pi)}")
    print(f"math.radians(180)         = {math.radians(180)}")
    print()
    print("Call get_area_of_lot() function with a different values, 5")
    print()
    print(f"get_area_of_lot(5, 10) = {get_area_of_lot(5, 10)}")
    print(f"get_area_of_lot(-16, 2) = {get_area_of_lot(-16.3, 2.5)}")
    print(f"get_area_of_lot(math.inf, 1) = {get_area_of_lot(math.inf, 1)}")
    print(f"get_area_of_lot('five', 'three') = {get_area_of_lot('five', 'three')}") # this string can't be multiplied in {area = length * width}, so an exception is thrown and an error message is printed out
    print()
    print("Call get_total_goals_scored() with various arguments")
    print(f"get_total_goals_scored([5, 2, 1, 0, 1]) = {get_total_goals_scored([5, 2, 1, 0, 1])}")
    print(f"get_total_goals_scored(1) = {get_total_goals_scored(1)}") # argument is not a list, so an exception is thrown
    print(f"get_total_goals_scored([]) = {get_total_goals_scored([])}") # list is empty so this will return 0, but an exception won't be thrown
    print(f"get_total_goals_scored(['one', 'two', three']) = {get_total_goals_scored(['one', 'two', 'three'])}") # strings cannot be summed, so an exception will be thrown
    print()
    print("Call calculate_accuracy() with a few arguments")
    print()
    print(f"calculate_accuracy(50, 100) = {calculate_accuracy(50, 100)}")
    print(f"calculate_accuracy(math.inf) = {calculate_accuracy(math.inf, 20)}")
    print(f"calculate_accuracy('one', 'two') = {calculate_accuracy('one', 'two')}")
    print()
    print("Call merch_plus_tax() with a few arguments")
    print()
    print(f"merch_plus_tax(100, 0.07) = {merch_plus_tax(100, 0.07)}")
    print(f"merch_plus_tax(100, math.inf) = {merch_plus_tax(100, math.inf)}")
    print(f"merch_plus_tax(100, 0) = {merch_plus_tax(100, 0)}")