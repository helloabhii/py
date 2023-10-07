import numpy as np
#imports the NumPy library and rename it as np so when we have to use write np instead of numpy
arry = np.array([1,3,7]) #creates a numpy 1-D array
print(arry) 

#

import numpy as np 
#range function
arry = np.arange(2) #0-2 exclude 2
print(arry) #[0,1]

#

import numpy as np
arry = np.linspace(0,10,8)
#0 = starting point
#10 = ending value
#8 = numbers how many parts you want
#np.linspace() used to generate sequence of evenly spaced numbers within a specified range
print(arry)

# Matplotlib library's

import numpy as np
import matplotlib.pyplot as plt
#imports the Matplotlib library's pyplot module 
#and gives it the alias plt
a = np.linspace(0,10,15)
b = np.arange(15)
print(a)
plt.plot(a,b)
plt.show()
#uses Matplotlib's plot() function to create a plot
#creates a line plot where a is the x-axis and b is the y-axis.
#plt.show() command will display the plot in a graphical window.

#Indexing and Slicing

import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) #1-D array
print(a[1]) #index 1 printed
print(a[1:15:5]) 
# This slicing expression starts at index 1, ends at index 15 (exclusive), and has a step of 5. 
# It means it will return values at indices 1, 6, and 11.
# So, this will print the array [ 2  7 12].
print(a[0:-1]) #prints from 0th index - last index exclude

#Playing with Indexes

import numpy as np
a = np.array([1,2,3,4,5,6,7])
print(a[1]+[3]) 
#[3] =  3-1=2 last exclude = in actual [1]+[2] = 2+3=5 

#shape Function()

import numpy as np
a = np.array([[1,2,3,4],[4,5,6,7]]) # 2-D array
# 2 Row and 4 Columns
print(a.shape) #returns a tuple
#(2, 4)
#The first element of the tuple represents the number of rows (which is 2)
#, and the second element represents the number of columns (which is 4).