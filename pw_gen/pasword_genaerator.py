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
        catatan = f"waktu pembuatan : {waktu_lenkap} | panjang karakter : {p} | simbol : {s}"
        self.aktivitas_pembuatan_sandi.append(catatan)
        with open("catatan_pw_gen.txt", "a") as simpan:
            simpan.write(f"{catatan}, \n")



    def baca_riwyat(self):
        with open("catatan_pw_gen.txt", "r") as baca:
            history = baca.read()
            return history





random_sandi = GenSandi()
print("------------------------------------")
print("SELAMAT DATANG DI PASSWORD GENERATOR")
print("------------------------------------")


while True:
    try:
        print("PILIHAN : ")
        print("0 : keluar")
        print("1 : membuat password")
        print("2 : melihat history pembuatan password")
        pilihan = input("\njadi apa yang mau anda lakukan? ")
        if pilihan == "0":
            print("\nterimakasih telah datang :)\n")
            break
        elif pilihan == "1":
            panjang = int(input("masukkan panjang sandi: "))
            if panjang <= 0:
                print("\n>>> panajangnya password gabisa 0 atau dibawahnya!\n")
                continue
            simbol = input("ketik \"y\" jika ingin menggunakan simbol: ").lower() == "y"
            hasil = random_sandi.generate(panjang, simbol)
            print(f"\n{"-" * len(hasil)}\n{hasil}\n{"-" * len(hasil)}\n")
            random_sandi.catat_aktivitas(panjang, simbol)
        elif pilihan == "2":
            print(f"\nhistory:\n{random_sandi.baca_riwyat()}")
        else:
            print(f"\n>>> tolong masukan input yang seuai pilihan yah jangan \"{pilihan}\"\n")
    except ValueError as e:
        print(f"error = {e}")