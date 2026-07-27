#----- KALKULATOR PERHITUNGAN KELULUSAN -----#


nama = str(input("masukan nama siswa: "))
mapel = ["B.indo", "MTK", "B.ing", "sosiologi", "olahraga"]
data_nilai = {}

for nama_mapel in mapel:
    while True:
        nilai = int(input(f"masukkan nilai {nama_mapel}: "))
        if 0 <= nilai <=100:
            data_nilai[nama_mapel] = nilai
            break
        else:
            print("kamu harusmemasukan angka yang falid")
print(data_nilai)
#menghitug rata rata
perhitungan = round(sum(data_nilai.values()) / len(data_nilai.values()), 2)
print(f"nilai rata ratanya adalah: {perhitungan}")

if perhitungan >= 75:
    print(f"sellamat {nama} kamu lulus! ")
elif perhitungan >= 70:
    print(f"{nama} kamu harus melakukan remidi agar bisa lulus ")
else:
    print(f"mohon maaf {nama} anda dinyatakn tidak lulus ")

#    for key, value in data_siswa.items():
#        print(f"{key} : {value}")