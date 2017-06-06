#Launch IDE as 'python -i _utilities.py'
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy import dtype
import matplotlib as mplt
import matplotlib.pyplot as plt
import pylab
import os

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>To print():
def p(the_var, str_representation='NOT SUPPLIED'):
    print('-' * 20 + ' ', end='')
    print(str_representation + ':')
    print(the_var)
    print('=' * 10)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>To exit() IDE:
def e():
    exit()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>To clear() screen:
def c():
    os.system('cls' if os.name == 'nt' else 'clear')
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>To print():
def _p(the_var, str_representation='NOT SUPPLIED'):
    print('-' * 20 + ' ', end='')
    print(str_representation + ':')
    print(the_var)
    print('=' * 10)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>To exit() IDE:
def _e():
    exit()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>To clear() screen:
def _c():
    os.system('cls' if os.name == 'nt' else 'clear')
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
