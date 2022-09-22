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
