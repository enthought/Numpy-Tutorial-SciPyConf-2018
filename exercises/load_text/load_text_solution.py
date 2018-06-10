"""
Load Array from Text File
-------------------------

0. From the IPython prompt, type::

        In [1]: loadtxt?

   to see the options on how to use the loadtxt command.


1. Use loadtxt to load in a 2D array of floating point values from
   'float_data.txt'.  The data in the file looks like::

        1 2 3 4
        5 6 7 8

   The resulting data should be a 2x4 array of floating point values.

2. In the second example, the file 'float_data_with_header.txt' has
   strings as column names in the first row::

        c1 c2 c3 c4
         1  2  3  4
         5  6  7  8

   Ignore these column names, and read the remainder of the data into
   a 2D array.

   Later on, we'll learn how to create a "structured array" using
   these column names to create fields within an array.

Bonus
~~~~~

3. A third example is more involved. It contains comments in multiple
   locations, uses multiple formats, and includes a useless column to
   skip::

    -- THIS IS THE BEGINNING OF THE FILE --
    % This is a more complex file to read!

    % Day,  Month,  Year, Useless Col, Avg Power
       01,     01,  2000,      ad766,         30
       02,     01,  2000,       t873,         41
    % we don't have Jan 03rd!
       04,     01,  2000,       r441,         55
       05,     01,  2000,       s345,         78
       06,     01,  2000,       x273,        134 % that day was crazy
       07,     01,  2000,       x355,         42

    %-- THIS IS THE END OF THE FILE --
"""

from __future__ import print_function
from numpy import loadtxt

#############################################################################
# 1. Simple example loading a 2x4 array of floats from a file.
#############################################################################
ary1 = loadtxt('float_data.txt')

print('example 1:')
print(ary1)


#############################################################################
# 2. Same example, but skipping the first row of column headers
#############################################################################
ary2 = loadtxt('float_data_with_header.txt', skiprows=1)

print('example 2:')
print(ary2)

#############################################################################
# 3. More complex example with comments and columns to skip
#############################################################################
ary3 = loadtxt("complex_data_file.txt", delimiter=",", comments="%",
               usecols=(0, 1, 2, 4), dtype=int, skiprows=1)

print('example 3:')
print(ary3)
