## operasi aritmatika

import numpy as np

'''
operasi aritmatika di bawah tidak sesuai dengan 
aturan aritmatika matrik pada matrmatika
'''
# 2 dimensi
print("="*10+"matrik a dan b")
cnp = np.array([(1,2,3), (4,5,6)])
dnp = np.array([(7,8,9), (-1,-2,-3)])
print("matrik a:\n",cnp)
print("matrik b:\n",dnp)

    # penjumlahan
print("="*5 + "penjumlahan matrik (a+b)")
hasil = cnp + dnp
print(hasil)
    # perkurangan
print("="*5 + "pengurangan matrik (a-b)")
hasil = cnp - dnp
print(hasil)
