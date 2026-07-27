#---------------------------------------------------------------------#
# print("Program Menghitung Luas Persegi Panjang")
# panjang = int(input("Masukkan panjang: "))
# lebar = int(input("Masukkan lebar: "))
# luas = (panjang * lebar)
# print(panjang, "*", lebar, "jadi Luas persegi panjang adalah: ", luas)

#---------------------------------------------------------------------#
# and kalau semua true maka hasilnya true, kalau salah satu false maka hasilnya false
# x = 10
# print(x == 10 and x < 9)
# print(x > 4 and x < 11 and x != 5)
# or kalau salah satu true maka hasilnya true, kalau semua false maka hasilnya false
# print(x == 10 or x < 9 or x != 5)
# not kalau true maka hasilnya false, kalau false maka hasilnya true
# he_is_raining = False
# print(not he_is_raining)
# print(not (x > 4 and x < 11 and x == 5))

# 1.    not (Prioritas tertinggi, dikerjakan paling awal)
# 2.    and (Prioritas menengah)
# 3.    or (Prioritas terendah, dikerjakan paling akhir)
# print(True or False and not True)
# true or False and (not True)
# true or (False and False)
# (true or False)
# true

#---------------------------------------------------------------------#
#SISTEM SAPAAN DENGAN F STRING

#    x = "    Belajar PYTHON_hayuk        "
#    print(f"hallo",x.upper())
#    print(f"hallo",x.lower())
#    print(f"(bentuk strip) hallo",x.strip()) # menghapus spasi (hanya yang ad du akhir dan awl)
#    print(f"(bentuk split) hallo",x.split()) # membuat tabel
#    print(f"(bentuk replace) hallo",x.replace("Belajar", "ngajarin")) # menganti

#    v = input(str("hallo siapa namamu: "))
#    print(f"ohh hallo ",v.upper())

#---------------------------------------------------------------------#
#Percabangan (Conditional)
#    nama = str(input("tolong masukkan nama anda: "))
#    nilai = int(input("tolong masukkan nilai anda: "))

#    if nilai > 75:
#        print(f"{nama} dengan nilai {nilai} kamu lulus")
#    elif nilai < 70:
#        print(f"{nama} dengan nilai {nilai} mohon maaf kamu tidak lulus")
#    else:
#        print(f"'{nama.upper()}' dengan nilai '{nilai}' kamu perlu remidi agar lulus")

#---------------------------------------------------------------------#

#   for i in range(10):
#       print(i)

#    nama_nama = []
#    banyaknya_nama = int(input("ada berapa banyak data nya: "))
#    for i in range(banyaknya_nama):
#        nama = input(f"masukkan data ke-{i+1}: ")
#        nama_nama.append(nama)
#    print(nama_nama)

#    y = 1
#    while y <= banyaknya_nama:
#        print(f"ada-{nama_nama}")
#        y = y + 1

#    for i in range(1,10):
#        if i % 2 == 0:
#            continue
#        print(f"{i} ini adalah angka ganjil")
#    for i in range(1,10):
#        if i % 8 == 0:
#            print(f"ketemu {i}")
#            break
#        print(f"belum ketemu {i} : 3 != 0")###

#    for y in range(1,20):
#        if y == 15:
#            break
#        if y % 3 == 0:
#            continue
#        print(y)
#---------------------------------------------------------------------#
buah = ["apel", "jeruk", "mangga", "pisang"]

print(buah[0])   # apel
print(buah[1])   # jeruk
print(buah[3])   # pisang
print(buah[-1])  # pisang (index negatif = hitung dari belakang)
print(buah[-2])  # mangga

buah.append("anggur")
print(buah)  # ['apel', 'jeruk', 'mangga', 'pisang', 'anggur']

buah.remove("jeruk")
print(buah)  # ['apel', 'mangga', 'pisang', 'anggur']

angka = [10, 20, 30, 40, 50]

print(angka[0:3])   # [10, 20, 30]  -> index 0,1,2 (index 3 gak ikut)
print(angka[1:4])   # [20, 30, 40]
print(angka[:2])    # [10, 20]      -> dari awal sampai index 2 (gak termasuk)
print(angka[2:])    # [30, 40, 50]  -> dari index 2 sampai akhir
print(angka[:])     # [10, 20, 30, 40, 50]  -> copy semua

siswa = {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}
# nama = key dan budi = valuenya
print(siswa["nama"])     # Budi
print(siswa["umur"])     # 20

print(siswa.get("nama"))          # Budi
print(siswa.get("alamat"))        # None (gak error)
print(siswa.get("alamat", "Tidak ada data"))  # Tidak ada data (pakai default)

#ambil semua key
print(siswa.keys())  # dict_keys(['nama', 'umur', 'jurusan'])
#ambil semua value
print(siswa.values())  # dict_values(['Budi', 20, 'Informatika'])
#ambil keduanya
print(siswa.items())

#pakai loop
for key in siswa.keys():
    print(key)
# Output: nama, umur, jurusan (masing-masing baris baru)

for value in siswa.values():
    print(value)
# Output: Budi, 20, Informatika

for key, value in siswa.items():
    print(f"{key}: {value}")
# Output:
# nama: Budi
# umur: 20
# jurusan: Informatika

for pair in siswa.items():
    print(pair)         # ('nama', 'Budi'), ('umur', 20), dst — masih dalam bentuk tuple
    print(pair[0])       # 'nama' (key-nya)
    print(pair[1])       # 'Budi' (value-nya)

# Ini sama hasilnya, tapi lebih langsung dengan unpacking:
for key, value in siswa.items():
    print(key)    # 'nama'
    print(value)  # 'Budi'