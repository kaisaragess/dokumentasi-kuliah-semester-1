#input 
pembeli = input("Input Nama Pembeli : ")
no_hp = input("Input No. Handphone : ")
jurusan = input("Input Jurusan [SBY/BL/LMP] : ")

#proses
if jurusan == "sby" or "SBY" :
    namajurusan = "Surabaya"
    harga = 300000
elif jurusan == "BL" or "bl" :
    namajurusan = "Bali"
    harga = 500000

#input jumlah beli
jumlah = int(input("Masukkan Jumlah Beli : "))

#proses potongan 
if jumlah >= 3 :
    potongan = (jumlah*harga)*0.1
else :
    potongan = 0

total = (jumlah*harga)-potongan

#output
print("------------------------------------")
print("{:^40}".format("Penjualan Tiket Bus"))
print("{:^40}".format("XYZ"))
print("------------------------------------")
print("Nama Pemebeli        : " + str(pembeli))
print("No. Handphone        : " + str(no_hp))
print("Kode Jurusan yang Dipilih : " +(namajurusan))
print("Harga                :",harga)
print("Jumlah Beli          :", + (jumlah))
print("------------------------------------")
print("potongan yang didapat : ", potongan)
ubay = int(input("Masukkan Uang Bayar : ")) #input uang bayar
uangkembali = ubay-total
print("Uang Kembali : ", uangkembali)
