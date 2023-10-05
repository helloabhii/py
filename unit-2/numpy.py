import numpy as np
arry = np.array([1,3,7])
print(arry)

import numpy as np 
#range function
arry = np.arange(2)
print(arry)

import numpy as np
arry = np.linspace(0,10,8)
print(arry)

import numpy as np
import matplotlib.pyplot as plt
a = np.linspace(0,10,15)
b = np.arange(15)
print(a)
plt.plot(a,b)

import numpy as np
a = np.array([1,2,3,4,5,6])
print(a[1])
print(a[1:4:5])
print(a[0:-1])

import numpy as np
a = np.array([1,2,3,4,4,5,6,7])
print(a[1]+[5])

import numpy as np
a = np.array([[1,2,3,4],[4,5,6,7]])
print(a.shape)