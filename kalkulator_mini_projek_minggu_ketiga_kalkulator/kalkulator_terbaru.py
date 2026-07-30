class kalkulator:
    def __init__(self):
        self.riwayat = []

    def tambah(self, a, b):
        hasil = a + b
        catatan = f"{a} + {b} = {hasil}"
        self.riwayat.append(catatan)
        with open("history.txt", "a") as simpen:
            simpen.write(f"{catatan} \n")
        return hasil

    def kurang(self, a, b):
        hasil = a - b
        catatan = f"{a} - {b} = {hasil}"
        self.riwayat.append(catatan)
        with open("history.txt", "a") as simpen:
            simpen.write(f"{catatan} \n")
        return hasil

    def kali(self, a, b):
        hasil = a * b
        catatan = f"{a} x {b} = {hasil}"
        self.riwayat.append(catatan)
        with open("history.txt", "a") as simpen:
            simpen.write(f"{catatan} \n")
        return hasil

    def bagi(self, a, b):
        if b == 0:
            return " angka tidak boleh nol"
        else:
            hasil = a / b
            catatan = f"{a} / {b} = {hasil}"
            self.riwayat.append(catatan)
            with open("history.txt", "a") as simpen:
                simpen.write(f"{catatan} \n")
            return hasil

    def baca_riwyat(self):
        with open("history.txt", "r") as baca:
            baca_txt = baca.read()
            return baca_txt

masuk = kalkulator()
print("\n","="*45)
print("\n  kamu sekarang sedang memakai kalkulator 1,1".upper())
print("\n","="*45)
while True:
    print("0. keluar daari permainan")
    print("00. untuk membuka history")
    print("1. pertambahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")
    try:
        pilihan = input("pilih: ")
        if pilihan == "0":
            print("\n--- terimakasih telah bermain ---\n")
            break
        if pilihan == "00":
            print(f"\nriwayat: \n\n{masuk.baca_riwyat()}")
            break
        if pilihan in ("1", "2", "3", "4"):
            angka1 =  int(input(f"masukkan angka pertama: "))
            angka2 = int(input(f"masukan angka kedua: "))
            if pilihan == "1":
                print(f"---\n{angka1} + {angka2} = {masuk.tambah(angka1 , angka2)}\n---")
            elif pilihan == "2":
                print(f"---\n{angka1} - {angka2} = {masuk.kurang(angka1 , angka2)}\n---")
            elif pilihan == "3":
                print(f"---\n{angka1} x {angka2} = {masuk.kali(angka1 , angka2)}\n---")
            elif pilihan == "4":
                print(f"---\n{angka1} / {angka2} = {masuk.bagi(angka1 , angka2)}\n---")
        else:
            print(("\n --- pilihlah dari angka 0-4 ---\n").upper())
    except ValueError as e:
        print(f"---\n | {("tolong masukan input yang sesuai").upper()} | error = {e}\n---")