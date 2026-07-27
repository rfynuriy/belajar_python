
class produk():
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok
    def total_nilai_barang(self):
        return f"total harganilai barangnya = {(self.stok * self.harga): ,}Rp"
    def info(self):
            return f" barang = {self.nama}, harga = {self.harga}, stok = {self.stok}"

produk1 = produk("shampo", 40000, 24)
produk2 = produk("sabun", 5000, 30)
daftar_produk = [produk1, produk2]

print(produk1.total_nilai_barang())
print(produk2.total_nilai_barang())
print(produk1.info(), produk2.info())



