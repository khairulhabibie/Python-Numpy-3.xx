## indexing, slicing, and itarasi

import numpy as np

# matrik a
print("="*15+"matrik a")
a = np.arange(10)**2
print("matrik a",a,"\n")

# indexing : mengambil nilai pada indeks tertentu
print("="*10+"indexing matrik a")
print("index ke-1:", a[0])          # data ke 0
print("index ke-7:", a[6])          # data ke 6
print("index terkahir:", a[-1], "\n")   # data terakhir

# slicing : mengambil nilai dengan urutan tertentu
print("="*10+"slicing matrik a")   
print("slice 1-6:", a[0:6])         # data 1 sampai 6
print("slice 4-terakhir:", a[3:])   # data 3 sampai ter-akhir
print("slice awal-5", a[:5], "\n")  # data awal sampai 5

# iterasi : melakukan loop "for" untuk mengambil data
print("="*10+"iterasi matrik a")
for i in a:
    print("nilai =",i)


