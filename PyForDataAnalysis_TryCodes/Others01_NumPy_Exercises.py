# a. Import the "numpy" library as "np".
import numpy as np
from numpy import dtype
import matplotlib as mplt
import matplotlib.pyplot as plt
import pylab
from _utilities import p

# b. Create a list with values 1 to 10 and assign it to the variable "x".
x = range(1,11)

# c. Create an integer array from "x" and assign it to the variable "a1".
a1 = np.array(x,'i')
print(a1)
# d. Create an array of floats from "x" and assign it to the variable "a2".
a2 = np.array(x,'f')

# e. Print the data type of each array (use the attribute "dtype").
print(a1.dtype)
print(a2.dtype)

#2:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# a. Create an array of shape (2, 3, 4) of zeros.
my_arr = np.zeros((2,3,4))
p(my_arr, 'my_arr')
# b. Create an array of shape (2, 3, 4) of ones.
# c. Create an array with values 0 to 999 using the "np.arange" function.
p(np.minimum(x,21))