## cara advanced membuat matrik

import numpy as np

# dengan tipe data tertentu
print("="*10+"dengan tipe tertentu")
a1 = np.array([(1,2,3),(4,5,6)], dtype = float)
a2 = np.array([(1,2,3),(4,5,6)], dtype = int)
print("tipe float:\n",a1)
print("tipe integer:",a2)

# dengan fungsi
print("="*10+"dengan fungsi")
    # penulisan fungsi
def kuadrat(baris, kolom):                              # argumen baris dan kolom harus ada
    return kolom**2
def jumlah(baris, kolom):
    return (baris+kolom)
    # memanggil fungsi kuadrat
b1 = np.fromfunction(kuadrat,(1,10), dtype = int)       # data matrik 0 - 9
print("kuadrat:\n",b1)    
    # memanggil fungsi jumlah
c = np.fromfunction(jumlah,(4,4), dtype = float)        # matrik 4x4
print("baris + kolom:\n",c)

# dengan iterable
print("="*10+"dengan iterable")
iterable = (x*2 for x in range(5))                      # dengan iterasi 0 - 4
d = np.fromiter(iterable, dtype = int)
print(d)

# dengan array yang di costum
print("="*10+"multi array (costum)")
dtipe = [("nama","S255"),("tinggi",int)]
data = [("khairul", 150),("habibie", 160),("khair",170)]
e = np.array(data, dtype = dtipe)
print(e[0])                                             # ambil data ke 0