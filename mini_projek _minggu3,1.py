"""
try:
    angka1 = int(input("hello masukan angka pertama: "))
    angka2 = int(input("masukkan angka kedua: "))
    print(f"hasil baginya adalah: {angka1 / angka2:.2f}")
except ValueError as e:
    print(f"input yang diberikan tidak falid! {e}: ")
except ZeroDivisionError:
    print("angka tak boleh 0")
#"""

#"""

hasil = ""
try:
    angka1 = int(input("hello masukan angka pertama: "))
    angka2 = int(input("masukkan angka kedua: "))
    hasil= f"{angka1 / angka2:.2f}"
except ValueError as e:
    print(f"input yang diberikan tidak falid! {e}: ",)
except ZeroDivisionError:
    print("angka tak boleh 0")
else:
    print(f"input yang dimasukan falid {angka1} / {angka2}")
finally: # ini akan tetap maksa keluar mau hasil reor atau tidak dia gapeduli
    print(f"hasil = {hasil}")
#"""