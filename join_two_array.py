import numpy as np
n1 = np.array([1,2,3,4])
n2 = np.array([9,8,7,6])

np.vstack([n1,n2])
#array([[1, 2, 3, 4],
#       [9, 8, 7, 6]])
np.hstack([n1,n2])#array([1, 2, 3, 4, 9, 8, 7, 6])
