## perkalian vektor (dot dan cross) ~ 1 dimensi

import numpy as np

# perkalian dot (a,b)
print("="*10+"perkalian dot (a.b)")
a = np.array([1,3])         
b = np.array([2,1])         
print("vektor a:\n",a)
print("vektor b:\n",b)
    # perkalian dot
c = np.dot(a,b)
print("Hasil:\n",c)

# perkalian cross (c,d)
print("="*10+"perkalian cross (dxe)")
d = np.array([1,2,0])
e = np.array([2,1,0])
print("vektor d:\n",d)
print("vektor e:\n",e)
    # perkalian cross
f = np.cross(d,e)
print("Hasil:\n",f)