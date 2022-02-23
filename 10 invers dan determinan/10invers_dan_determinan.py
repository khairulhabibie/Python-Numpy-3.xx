## invers dan determinan

import numpy as np

# matrik a
a = np.array([(1,-1),(1,1)])
print("="*10+"matrix a:\n",a)

# invers matrix a (a_inv)
a_inv = np.linalg.inv(a)
print("="*10+"invers matrik a:\n",a_inv)

# matrik a dot a_inver
hasil = np.dot(a,a_inv)
print("="*10+"a dot a_inv:\n",hasil)

# determinan a (a_det)
det_a = np.linalg.det(a)
print("="*10+"det matrix a:\n",det_a)

# determinan matrix a_invers (det_a_inv)
det_a_inv = np.linalg.det(a_inv)
print("="*10+"det matrix a_inv_det:\n",det_a_inv)


