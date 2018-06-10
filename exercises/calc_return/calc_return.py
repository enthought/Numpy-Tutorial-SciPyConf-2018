"""
Calc return
===========

For a given stock, the return is connected to its close price p by

         p(t) - p(t-1)
ret(t) = -------------
             p(t-1)

The close price for Apple stock for all business days in 2008 is loaded for you
from the data file `aapl_2008_close_values.csv`.

1. Use these values to compute the corresponding daily return for every
business day of that year (except the first one).

2. Plot these returns, converted to percentages, over the course of the year.
On the same plot, draw a red line at 0.

Note: a for loop is neither necessary nor recommended for this calculation

Bonus
~~~~~
3. There is some blank space in the plot made in question 2 because by default,
matplotlib displays plots with a range along the x axis that is larger than the
highest x coordinate. Use IPython to learn about matplotlib's `plt.xlim` function
and make the limits of your plot tighter.
"""
from __future__ import print_function
from numpy import arange, loadtxt, zeros
import matplotlib.pyplot as plt

prices = loadtxt("aapl_2008_close_values.csv", usecols=[1], delimiter=",")

print("Prices for AAPL stock in 2008:")
print(prices)
