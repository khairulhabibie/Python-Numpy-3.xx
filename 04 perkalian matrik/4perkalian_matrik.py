## perkalian matrik

import numpy as np

'''
perkalian package numpy sesuai dengan aturan dasar
perkalian matrik pada matematika")
'''
# matrik a dan b
print("="*10+"matrik a dan b")
a = np.array([(1,2),(3,4)])             # matrik biasa
b = np.ones([2,2])                      # matrik satuan dengan ordo 2x2
print("matrik a:\n",a)
print("matrik b:\n",b)

# perkalian matrik a dan b
print("="*10+"perkalian matrik a dan b")
c1 = np.dot(a,b)        # cara 1
'''
c1 = a.dot(b)           # cara 2
'''
print("matrik c1:")
print(c1)