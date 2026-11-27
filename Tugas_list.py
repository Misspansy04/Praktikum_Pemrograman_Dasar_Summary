#List Penumpang
penumpang = ["William", "Kate", "Anderson", "Jame", "Mady"]
print("Data Penumpang:", penumpang)
#Menambahkan Jones dalam list
penumpang.append ("Jones")
print("Jones ditambahkan:", penumpang)
#Mengganti Anderson dengan Grace
penumpang[2] = "Grace"
print ("Anderson diganti Grace:", penumpang)
#Mengecek apakah ada nama Thampson dalam list
member = "Thompson" in penumpang
print("Apakah Thompson ada dalam list penumpang?:", member)
#Urutan nama penumpang berdasarkan abjad
sorted = penumpang
print("urutan penumpang:", penumpang)
#Penumpang yang sudah sampai di Yogyakarta
for nama in penumpang:
    print("Siapa saja yang sudah sampai di Yogyakarta?:", nama)
#Mengosongkan list
penumpang.clear()
print("Penumpang sudah turun, kereta kembali ke Jakarta:", penumpang)