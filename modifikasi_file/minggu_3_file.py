
"""

f = open("apapun.txt", "w")
f.write("hallo ini adalah baris pertama\n")
f.write("ini merupakan baris kedua\n")
f.close()

b = open("apapun.txt", "r") # buka ( "<file>" "<perintah>")
isi = b.read() # fariable = perintah baca
print(isi) # esekusi fariable
b.close() # tutup

with open("apapun.txt", "r") as fariable: # buka lalu tutup
    cek = fariable.read() # pembuatan fariable = perintah baca
    print(cek) # eksekusi fariable

#"""

"""
PERINTAH

"r" - Read   - baca file (file harus udah ada, kalau gak ada, error)
"w" - Write  - tulis ke file (kalau file udah ada, isi lama akan HILANG/ketimpa; kalau belum ada, file baru dibuat)
"a" - Append - tambah data di akhir file (isi lama tetap ada, data baru ditambahin di bawahnya)
"x" - Create - bikin file baru (error kalau file udah ada duluan)
tambahan
"r+" - Baca dan tulis (file harus udah ada)
"w+" - Tulis dan baca (isi lama tetap ke-hapus, kayak mode "w" biasa)
"a+" - Tambah (append) dan baca (isi lama tetap ada)
"""


isi_manual = str(input("mengatik: "))
with open("apapun.txt", "a") as fung:
    fung.write(f"{isi_manual}\n")

with open("apapun.txt", "r") as bca:
    baca = bca.read()
    print(baca)