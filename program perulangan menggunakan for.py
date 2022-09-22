# Percabangan
bottle_milk_count = 173
egg_count = 1000

print(f"Jumlah botol susu {bottle_milk_count} botol")
print(f"Jumlah telur {egg_count} butir")

if bottle_milk_count > 0:
    print("budi mengecek harganya , ternyata uangnya cukup")
    if egg_count == 1000:
        print("Budi membeli 100 botol susu")
    else:
        print("budi membeli 6 botol susu")
else:
    print("budi tidak jadi membeli botol cucu")

# Perulangan

jumlah_buku = 10
print("ibu menuruh untuk membaca semua buku")

jumlah_buku_yang_sudah_dibaca= 0
print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}")

for jumlah_buku_yang_sudah_dibaca in range(1, jumlah_buku+1):
    print(f"buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print(jumlah_buku_yang_sudah_dibaca)

