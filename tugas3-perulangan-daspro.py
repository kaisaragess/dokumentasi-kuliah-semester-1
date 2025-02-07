# Header
print('''
      GEROBAK FRIED CHICKEN
----------------------------------
Kode     Jenis Potong        Harga
----------------------------------
D        Dada                Rp2.500
P        Paha                Rp2.000
S        Sayap               Rp1.500
----------------------------------''')

# Inisiasi variabel
jenis_potong = []
harga_satuan = []
byk_beli = []
jumlah_harga = []

# Proses
byk_pesanan = int(input("Banyak pesanan = "))

for i in range(byk_pesanan):
    print(f"Pesanan Ke - {i+1}")
    while True:
        input_kd_ptg = input("Kode Potong (D/P/S) = ").upper()
        if input_kd_ptg in ["D", "P", "S"]:
            break
        print("Kode tidak valid. Masukkan D, P, atau S.")

    if input_kd_ptg == "D":
        jenis_potong.append("Dada")
        harga_satuan.append(2500)
    elif input_kd_ptg == "P":
        jenis_potong.append("Paha")
        harga_satuan.append(2000)
    elif input_kd_ptg == "S":
        jenis_potong.append("Sayap")
        harga_satuan.append(1500)

    while True:
        try:
            byk_beli.append(int(input("Banyak Potong = ")))
            break
        except ValueError:
            print("Masukkan angka yang valid.")

# Hitung jumlah harga
for j in range(byk_pesanan):
    jumlah_harga.append(harga_satuan[j] * byk_beli[j])

# Output
print('''
===================================================================================
No.     Jenis Potong     Harga Satuan     Banyak Beli      Jumlah Harga
===================================================================================
''')

for k in range(byk_pesanan):
    print(f"{k+1} \t {jenis_potong[k]} \t\t Rp{harga_satuan[k]} \t\t {byk_beli[k]} \t\t Rp{jumlah_harga[k]}")

print("====================================================================================")

# Hitung total bayar
jumlah_bayar = sum(jumlah_harga)
pajak = jumlah_bayar * 0.1
total_bayar = jumlah_bayar + pajak

print(f"Jumlah bayar \t Rp{jumlah_bayar}")
print(f"Pajak 10% \t Rp{pajak}")
print(f"Total Bayar \t Rp{total_bayar}")
