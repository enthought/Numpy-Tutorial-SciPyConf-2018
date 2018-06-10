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
"""
from numpy import dtype, loadtxt, float64, NaN, isfinite, all
import matplotlib.pyplot as plt

# Open the file.
log_file = open('short_logs.crv')

# 1.Create a dtype from the names in the file header.
header = log_file.readline()
log_names = header.split()

# Construct the array "dtype" that describes the data.  All fields
# are 8 byte (64 bit) floating point.
fields = list(zip(log_names, ['f8']*len(log_names)))
fields_dtype = dtype(fields)

#2. Use loadtxt to load the data into a structured array.
logs = loadtxt(log_file, dtype=fields_dtype)

# 3. Make a 2D, float64 view of the data.
#    The -1 value for the row shape means that numpy should
#    make this dimension whatever it needs to be so that
#    rows*cols = size for the array.
values = logs.view(float64)
values.shape = -1, len(fields)

# 4. Relace any values that are -999.25 with NaNs.
values[values==-999.25] = NaN

# 5. Make a mask for all the rows that don't have any missing values.
#    Pull out these samples from the logs array into a separate array.
data_mask = all(isfinite(values), axis=-1)
good_logs = logs[data_mask]


# 6. Plot VP vs. VS for the "complete rows.
plt.plot(good_logs['VS'], good_logs['VP'], 'o')
plt.xlabel('VS')
plt.ylabel('VP')
plt.show()
