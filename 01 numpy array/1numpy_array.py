## membuat numpy matrik

import numpy as np

# matrik 1 dimensi
print("="*10+"array")
a = np.array([1,2,3,4,5,])
print(a)

# vektor dengan arange
print("="*10+"vektor dengan arange")
b = np.arange(1,10,0.5)
print(b)

# linspace
print("="*10+"linspace")
c = np.linspace(1,10,4)
print(c)

# matrik 2 dimensi
print("="*10+"multidimensi matrik")
e = np.array([(1,2,3), (4,5,6)])
print(e)

# matrik nol atau zero
print("="*10+"matrik nol atau zero")
f = np.zeros((5,5))             # ordo matrik 5x5
print(f)

# matrik satuan
print("="*10+"matrik satuan")
g = np.ones((5,5))              # ordo matrik 5x5
print(g)

# matrik identitas
print("\n" + "="*5 + "matrix identitas")
h = np.identity(5)      # cara 1    # matrik 5x5
'''
h = np.eye(5)           # cara 2    # matrik 5x5
'''
print(h)




