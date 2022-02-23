## stacking matrik atau menumpuk matrik

import numpy as np

# 1 dimensi
print("="*10+"matrik 1 dimensi:")
a1 = np.array([1,2,3])
b1 = np.array([4,6,7])
print("matrik a1:\n",a1)
print("matrik b2:\n",b1)

    # stacking matrik a1 dan b1
print("="*10+"stacking matrik a dan b")
c1 = np.hstack((a1,b1))     # horizontal
d1 = np.vstack((a1,b1))     # vertikal
print("hstack:\n",c1)
print("vstack:\n",d1)

# 2 dimensi
print("="*10+"matrik 2 dimensi")
a2 = np.zeros((2,2))
b2 = np.ones((2,2))
print("matrik a2:\n",a2)
print("matrik b2:\n",b2)

    # stacking matrik a2 dan b2
print("="*10+"stacking matrik a2 dan b2")
c2 = np.hstack((a2,b2))     # horizontal ~ jumlah baris harus sama
d2 = np.vstack((a2,b2))     # vertikal ~ jumlah kolom harus sama
print("hstack:\n",c2)
print("vstack:\n",d2)

