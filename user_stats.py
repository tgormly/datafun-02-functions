"""
Tim Gormly
1/24/2023
44-608 Data Analytics Fundamentals
Module 2

This example illustrates basic analytics
using just the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

To update, try:
conda update pythnon -y
conda --version

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

"""

import statistics

# define a variable with some univariant data 
# (one varabile, many readings)
scores = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

scores_mean = statistics.mean(scores)
scores_median = statistics.median(scores)
scores_mode = statistics.mode(scores)
scores_variance = statistics.variance(scores)
scores_standard_deviation = statistics.stdev(scores)

print(f"Mean: {scores_mean:0.2f}")
print(f"Median: {scores_median:0.2f}")
print(f"Mode: {scores_mode}")
print(f"Variance: {scores_variance:0.2f}")
print(f"Standard Deviation: {scores_standard_deviation:0.2f}")

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
x_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_temps = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31, 32]

slope, intercept = statistics.linear_regression(x_times, y_temps)

# print(f"Slope: {slope}")
# print(f"Intercept: {intercept}")

y_future = (slope * 13) + intercept
print(f"At x_time 13, y_temp is predicted to be: {y_future:.2f} or {round(y_future)}")
