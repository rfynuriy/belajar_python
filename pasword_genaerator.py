import random
import string
from datetime import datetime

#   pw generator   #

class GenSandi:
    def __init__(self):
        self.aktivitas_pembuatan_sandi = []

    def generate (self, panjang, simbol):
        defauld = string.ascii_uppercase + string.ascii_lowercase + string.digits
        if simbol == True:
            defauld = defauld + string.punctuation
        karakter_terpilih = []
        for i in range(panjang):
            satu_karakter = random.choice(defauld)
            karakter_terpilih.append(satu_karakter)

        pw = "".join(karakter_terpilih)
        return pw


    def catat_aktivitas(self, p, s):
        sekarang = datetime.now()
        waktu_lenkap = sekarang.strftime("%d-%m-%Y %H:%M:%S")
        catatan = f"waktu pembuatan = \" {waktu_lenkap} \" | panjang karakter = {p} | simbol = {s}"
        self.aktivitas_pembuatan_sandi.append(catatan)
        with open("catatan_pw_gen.txt", "a") as simpan:
            simpan.write(f"{catatan}, \n")



    def baca_riwyat(self):
        pass




random_sandi = GenSandi()
while True:
    try:
        panjang = int(input("masukkan panjang sandi: "))
        simbol = input("ketik \"y\" jika ingin menggunakan simbol: ").lower() == "y"
        if simbol == True:
            break
        else:
            break
    except ValueError:
        print("tolong masukan angka")
print(random_sandi.generate(panjang, simbol))
