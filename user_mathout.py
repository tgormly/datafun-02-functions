# Explore some functions in the math module

# math.comb(5,1) = 5
# math.perm(5,1) = 5

# math.comb(5,3) = 10
# math.perm(5,3) = 60

# math.pi = 3.141592653589793

# math.degrees(2 * math.pi) = 360.0
# math.radians(180)         = 3.141592653589793

# Call get_area_of_lot() function with a different values, 5

# get_area_of_lot(5, 10) = 50
# get_area_of_lot(-16, 2) = -40.75
# get_area_of_lot(math.inf, 1) = inf
# Error: can't multiply sequence by non-int of type 'str'
# get_area_of_lot('five', 'three') = None

# Call get_total_goals_scored() with various arguments
# get_total_goals_scored([5, 2, 1, 0, 1]) = 9.0
# ERROR: object of type 'int' has no len()
# get_total_goals_scored(1) = None
# get_total_goals_scored([]) = 0
# ERROR: must be real number, not str
# get_total_goals_scored(['one', 'two', three']) = None

# Call calculate_accuracy() with a few arguments

# calculate_accuracy(50, 100) = 0.5
# The player scored more goals than they shot the puck!  Amazing!
# calculate_accuracy(math.inf) = inf
# ERROR: unsupported operand type(s) for /: 'str' and 'str'
# calculate_accuracy('one', 'two') = None

# Call merch_plus_tax() with a few arguments

# merch_plus_tax(100, 0.07) = 107.0
# merch_plus_tax(100, math.inf) = inf
# merch_plus_tax(100, 0) = 100