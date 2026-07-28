# eksekusi def #
import def_kalkulator



def kalkulator():
    print("\n","="*41)
    print("\n  kamu sekarang sedang memakai kalkulator".upper())
    print("\n","="*41)
    while True:
        print("0. keluar daari permainan")
        print("1. pertambahan")
        print("2. pengurangan")
        print("3. perkalian")
        print("4. pembagian")
        try:
            pilihan = input("pilih: ")
            if pilihan == "0":
                print("terimakasih telah bermain")
                break
            if pilihan in ("1", "2", "3", "4"):
                angka1 =  int(input(f"masukkan angka pertama: "))
                angka2 = int(input(f"masukan angka kedua: "))
                if pilihan == "1":
                    print(f"---\n{angka1} + {angka2} ={def_kalkulator.tambah(angka1 , angka2)}\n---")
                elif pilihan == "2":
                    print(f"---\n{angka1} - {angka2} ={def_kalkulator.kurang(angka1 , angka2)}\n---")
                elif pilihan == "3":
                    print(f"---\n{angka1} x {angka2} ={def_kalkulator.kali(angka1 , angka2)}\n---")
                elif pilihan == "4":
                    print(f"---\n{angka1} / {angka2} ={def_kalkulator.bagi(angka1 , angka2)}\n---")
            else:
                print(("\n pilihlah dari angka 0-4\n").upper())
        except ValueError as e:
            print(f"---\n | {("tolong masukan input yang sesuai").upper()} | error = {e}\n---")

kalkulator()
