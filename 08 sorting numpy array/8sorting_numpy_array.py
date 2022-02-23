## sorting numpy array

import numpy as np

# matrik 1 dimensi
print("="*10+"data random 1 dimensi")
a = np.floor(np.random.randn(1,6)*10)
print(a)
    # nilai maksimum dan minimum
print("="*10+"nilai maksimum dan minimum data random 1 dimensi")
print('nilai mak dari a =',a.max())         # nilai maksimum dari a
print('posisi mak dari a =',a.argmax())     # posisi maksium dari a
print('nilai min dari a =',a.min())         # nilai minimum dari a
print('posisi min dari a =',a.argmin())     # posisi minimum dari a
    # sorting : meng-urutkan nilai
print("="*10+"sorting nilai")
print('mengurutkan nilai dari a:')
print(np.sort(a))                   # meng-urutkan data a
print(np.argsort(a))                # index data a setelah diurutkan

# matrik 2 dimensi
print("="*10+"data random 2 dimensi")
a = np.floor(np.random.randn(2,2)*10)
print(a)
    # nilai maksimum dan minimum
print("="*10+"nilai maksium dan minimum data random 2 dimensi")
print('nilai mak dari a =',a.max())         # nilai maksimum dari a
print('posisi mak dari a =',a.argmax())     # posisi maksimum dari a
print('nilai mak dari a =',a.min())         # nilai minimum dari a
print('posisi mak dari a =',a.argmin())     # posisi maksimum dari a
    # sorting
print("="*10+"sorting nilai")
print('mengurutkan nilai dari a:')
print(np.sort(a))                   # meng-urutkan data : perbaris dimulai dari kiri ke kanan
print(np.argsort(a))                # index data a setelah diurutkan

# matrik costum
print("="*10+"data costum")
dtipe = [('nama','S10'),('nomor',int)]
data = [('kalium',20),('bromium',35),('helium',2)]
a = np.array(data, dtype = dtipe)
print(a)
    # sorting : meng-urutkan data
print("="*5+"sorting : berdasarkan nomor:") 
print(np.sort(a, order ='nomor'))
print("="*5+"sorting : berdasarkan nama:") 
print(np.sort(a, order ='nama'))



