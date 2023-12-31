#Program ini dibuat dengan menggunakan bahasa pemrograman python.
#Berisi contoh program sederhana proses pembelian voucher wifi.

#Struktur data dictionary
menu = {
    "4 jam" : 2000,
    "1 hari" : 5000,
    "1 minggu" : 12000,
    "1 bulan" : 35000
}

#Tampilan menu
print()
print("==========================================================")
print("====================== DAFTAR VOUCHER ====================")
print("==========================================================")
print()
for i in menu:
    print("Daftar Voucher : ", i,"\t Harga : ",menu[i])
print("Pembelian senilai Rp50000 atau lebih mendapatkan diskon 5%")
print("Silahkan dipilih sesuai dengan kebutuhan anda")
print()
print("==========================================================")
print("====================== Selamat Memesan ===================")
print("==========================================================")
print()
#Proses pembelian/pemesanan
beli = input("Silahkan pilih voucher (contoh 4 jam, 1 hari, dst) : ")
jumlah = int(input("Berapa jumlah voucher yang dibeli : "))
bayar = jumlah * menu[beli]

#Proses hitung jika pemesan mendapatkan diskon
if bayar >= 50000:
    diskon = bayar * 5 / 100
    total_bayar = bayar - diskon
    print("Selamat anda mendapatkan diskon 5%")
else:
    total_bayar = bayar

print()
#Rekap pembelian
print("==================================== Jenis Pesanan ===============================")
print("Daftar voucher : ",beli)
print("Jumlah yang dibeli : ",jumlah)
konfirmasi = int(input("Apakah semua sudah benar? (1)Ya, (2)Tidak. Silahkan pilih 1 atau 2: "))
print("==================================================================================")
print()

if konfirmasi == 1:
    print("==================================================================================")
    print("================================ Struk Pembayaran ================================")
    print("==================================================================================")
    print("Daftar voucher       : ",beli)
    print("Jumlah yang dibeli   : ",jumlah)
    print("Total harga          : ",bayar)
    print("Total bayar          : ",total_bayar)
    print()
    print("Selamat menikmati layanan internet kami, dan jangan lupa gunakan sebaik mungkin :)")
    print()
    print("==================================================================================")
    print("======================== Terimakasih Atas Kunjungan Anda =========================")
    print("==================================================================================")

else:
    print("Jika ada kesalahan, silahkan ulangi pembelian")


