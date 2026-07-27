
class produk():
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok
    def total_nilai_barang(self):
        return f"{(self.stok * self.harga): ,}"
    def banyaknya_barang(self):
        return f"jumlah barangnya ada -{len(self.barang)}"
    def info(self):
        return f" barang = {self.nama}, harga = {self.harga}, stok = {self.stok}"
produk1 = produk("shampo", 40000, 24)
produk2 = produk("sabun", 5000, 30)


print(produk1.total_nilai_barang())


