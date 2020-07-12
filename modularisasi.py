"""
program menghitung luas segitiga
luas segitiga =  alas x tinggi

"""
print('menghitung luas segitiga')
alas = 10
tinggi = 4

luas_segitiga = alas * tinggi/2
print(f"Segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas {luas_segitiga}\n")

print('membuat fungsi menghitung luas segitiga\n')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f'Menghitung segitiga dengan fungsi, hasilnya {hitung_luas_segitiga(10,6)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya {hitung_luas_segitiga(20,2)}')
