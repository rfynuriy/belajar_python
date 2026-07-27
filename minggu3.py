#    class Complex:
#        def __init__(self, nama, umur):
#            self.n = nama
#            self.u = umur

#x = Complex("rafi", 20)
#x2 = Complex("anne", 20)
#    print(x.n, x.u)
#    print(x.n, x2.n)


#class Siswa:
#    def __init__(self, nama, umur):
#        print("nocok")
#        self.nama = nama
#        self.umur = umur

#siswa1 = Siswa("Budi", 17)
#print(f"nama: {siswa1.nama} {siswa1.umur}")

class siswa:
    def __init__(self, nama, nilai_list):
        self.un = nama
        self.nill = nilai_list
    
    def hitung_rata_rata(self):
        return round(sum(self.nill) / len(self.nill), 2)
    def pennentuan_kelululusan(self):
        if self.hitung_rata_rata() >= 75:
            print(f"sellamat {self.un} kamu lulus! ")
        elif self.hitung_rata_rata() >= 70:
            print(f"{self.un} kamu harus melakukan remidi agar bisa lulus ")
        else:
            print(f"mohon maaf {self.un} anda dinyatakn tidak lulus ")

siswa1 = siswa("", [])

siswa1.un = input("siapa namamu: ")
siswa1.nill = [int(x) for x in input("berapa nilaimu [bindo, mtk, bing] (pisahkan degnan spasi): ").split()]

print(f"rata ratamu adalah -{siswa1.hitung_rata_rata()}")
siswa1.pennentuan_kelululusan()
