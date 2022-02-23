## operasi aritmatika

import numpy as np

'''
operasi aritmatika di bawah tidak sesuai dengan 
aturan aritmatika matrik pada matrmatika
'''
# 1 dimensi
print("="*5 + "matrik a dan b")
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])
print("matrik a :\n", anp)
print("matrik b :\n", bnp)

    # penjumlahan
print("="*5 + "penjumlahan matrik (a+b)")
hasil = anp + bnp
print(hasil)
    # pengurangan
print("="*5 + "pengurangan matrik (a-b)")
hasil = anp - bnp
print(hasil)
    # perkaliann
print("="*5 + "perkalian matrik (a*b)")
hasil = anp * bnp
print(hasil)
    # pembagian
print("="*5 + "pembagian matrik (a/b)")
hasil = anp / bnp
print(hasil)
    # kuadrat
print("="*5 + "kuadrat matrik a")
hasil = anp**2
print(hasil)