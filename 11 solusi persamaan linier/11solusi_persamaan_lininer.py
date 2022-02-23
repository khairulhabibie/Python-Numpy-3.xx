## solusi persamaan linier

import numpy as np

print("="*10+"persamaan linier:")
print("y1 = 2 . x1 + 3 . x2 = 23")
print("y2 =     x1 + 2 . x2 = 14")

a = np.array([(2,3),(1,2)])
y = np.array([23,14])
print("matrix a:")
print(a)

'''
y = ax
a_inv dot y = x
'''

a_inv = np.linalg.inv(a)
x = np.dot(a_inv,y)
print("solusi pers linier x1 dan x2:\n",x)