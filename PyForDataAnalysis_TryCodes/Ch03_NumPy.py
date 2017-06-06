import numpy as np
import matplotlib.pyplot as plt
import pylab
def p(the_var, str_representation='NOT SUPPLIED'):
   print('>' * len(the_var) + ' ', end='')
   print(str_representation + ':')
   print(the_var)
   print('<' * len(the_var))

def my_util(varia):
    for k, v in list(locals().items()):
      if v is varia:
        print('rrrrrrrrrrr')
        print(k)
        print(varia)

data = np.array([[ 0.9526, -0.246 , -0.8856], [ 0.5639, 0.2379, 0.9104]])
p(2 / data, '2/data')
p(data, 'data')
array_ones = (np.ones(8) * 2) 
p(array_ones)
sliced_array = array_ones[1:6]
sliced_array[:] = 4
print(sliced_array)
my_util(sliced_array[:])
# print(locals())
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
p(arr3d, 'arr3d')
p(arr3d[0], 'arr3d[0]')
p(arr3d[1], 'arr3d[1]')
p(arr3d[2], 'arr3d[2]')
