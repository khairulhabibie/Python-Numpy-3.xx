## manipulasi matrik

import numpy as np

# matrik a
print("="*10+"matrik a")
a = np.array([(1,2,3),(4,5,6)])
print("matrik a:\n",a)
print("ordo matrik a:",a.shape)

# transpose matrik a:
print("="*10+"transpose matrik a")
print(np.transpose(a))                      # cara 1
'''
print(a.transpose())                        # cara 2
print(a.T)                                  # cara 3
'''
print("matrik a dengan ukuran:",a.shape)

# flatten matrik a: baris matrik digabungkan menjadi 1 baris
print("="*10+"flatten matrik a")
print(np.ravel(a))                          # cara 1
'''
print(a.ravel())                            # cara 2
'''
print("matrik a dengan ukuran:",a.shape)

# reshape matrik a:
print("="*10+"reshape matrik a")
print(a.reshape(3,2))
print("matrik a dengan ukuran:",a.shape)

# resize matrik a: merubah ordo matrik a
print("="*10+"Resize Matrix a")
print(a.resize(3,2))
print("matrik a dengan ukuran:",a.shape)