"""
Structured Array
----------------

In this exercise you will read columns of data into a structured array using
loadtxt and combine that array to a regular array to analyze the data and learn
how the pressure velocity evolves as a function of the shear velocity in sound
waves in the Earth.

1. The data in 'short_logs.crv' has the following format::

       DEPTH          CALI       S-SONIC   ...
       8744.5000   -999.2500   -999.2500   ...
       8745.0000   -999.2500   -999.2500   ...
       8745.5000   -999.2500   -999.2500   ...

   Here the first row defines a set of names for the columns
   of data in the file.  Use these column names to define a
   dtype for a structured array that will have fields 'DEPTH',
   'CALI', etc.  Assume all the data is of the float64 data
   format.

2. Use the 'loadtxt' method from numpy to read the data from
   the file into a structured array with the dtype created
   in (1).  Name this array 'logs'

3. The 'logs' array is nice for retrieving columns from the data.
   For example, logs['DEPTH'] returns the values from the DEPTH
   column of the data.  For row-based or array-wide operations,
   it is more convenient to have a 2D view into the data, as if it
   is a simple 2D array of float64 values.

   Create a 2D array called 'logs_2d' using the view operation.
   Be sure the 2D array has the same number of columns as in the
   data file.

4. -999.25 is a "special" value in this data set.  It is
   intended to represent missing data.  Replace all of these
   values with NaNs.  Is this easier with the 'logs' array
   or the 'logs_2d' array?

5. Create a mask for all the "complete" rows in the array.
   A complete row is one that doesn't have any NaN values measured
   in that row.

   HINT: The ``all`` function is also useful here.

6. Plot the VP vs VS logs for the "complete" rows.

See :ref:`structured-array-solution`.
"""
from numpy import dtype, loadtxt, float64, NaN, isfinite, all
import matplotlib.pyplot as plt
# Open the file.
log_file = open('short_logs.crv')

# The first line is a header that has all the log names.
header = log_file.readline()
log_names = header.split()
