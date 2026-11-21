day1_membeli = {"keju","tepung","garam","gula","coklat"}
day2_membeli = {"garam","gula","coklat","kecap"}
print ("Pembelian hari pertama:", day1_membeli)
print ("Pembelian hari kedua:", day2_membeli)

day2_membeli.add("keju")
print ("Menambahkan keju pada pembelian hari kedua:", day2_membeli)

Barang_yang_sama_pada_pembelian = day1_membeli & day2_membeli
print ("Barang yang sama pada pembelian hari pertama dan kedua:", Barang_yang_sama_pada_pembelian)

Barang_yang_berbeda_pada_pertama = day1_membeli - day2_membeli
print ("Barang yang hanya di beli pada hari pertama:", Barang_yang_berbeda_pada_pertama)

day1_membeli.remove ("garam")
print ("setelah garam dihapus pada pembelian hari pertama:", day1_membeli)

Barang_yang_hanya_di_beli_pada_hari_kedua = day2_membeli - day1_membeli
print ("Barang yang hanya di beli pada hari kedua tapi tidak ada pada hari pertama:", Barang_yang_hanya_di_beli_pada_hari_kedua)