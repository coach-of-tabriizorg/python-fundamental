jumlah_buku = 10
print("ibu menyuruh untuk membaca semua buku")

jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
print(f"Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}")

while jumlah_buku_yang_sudah_dibaca_dan_dipahami < jumlah_buku:
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9:
        print(f"buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} belum paham")
    else:
        jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami + 2
        print(f"buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami")

print(f"buku yang sudah dibaca adalah {jumlah_buku_yang_sudah_dibaca_dan_dipahami}")