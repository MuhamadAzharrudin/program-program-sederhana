#Program ini dibuat dengan menggunakan bahasa pemrograman python.
#Berisi contoh program sederhana toko online perlengkapan rumah

jenis_produk = {
    1:"Lemari Kayu  ",
    2:"Sofa 1 Set   ",
    3:"Meja Makan   ",
    4:"Springbed    ",
    5:"Tirai 1 set",
    6:"Sapu lantai  ",
    7:"Kursi biasa  ",
    8:"Kulkas   ",
    9:"Televisi ",
    10:"Lemari Kaca "
}

daftar_harga = {
    1: 550000,
    2: 780000,
    3: 350000,
    4: 1500000,
    5: 30000,
    6: 10000,
    7: 20000,
    8: 4500000,
    9: 5000000,
    10: 850000
}

metode_pembayaran = {
    1:"Transfer",
    2:"Bayar Tunai (Langsung Ke Toko)",
    3:"Cash On Delivery (COD)"
}
print()
print("=============================================================================================")
print("======================================= DAFTAR PRODUK =======================================")
print("=============================================================================================")
print("Selamat datang di website toko kami")
print("Kami menyediakan beberapa produk dengan kualitas terbaik dan harga terjangkau")
print("Silahkan pilih produk yang anda inginkan")
print()
for i in jenis_produk:
    print("Id Product : ",i,"\t Nama Product : ",jenis_produk[i],"\t Harga Product : Rp",daftar_harga[i])
print("Pembelian diatas Rp5000000 akan mendapatkan diskon 10%")
print("=============================================================================================")
print("=============================================================================================")
print("=============================================================================================")
print()

pilih_id = int(input("Silahkan pilih Id product (contoh 1, 2, 3, dst): "))
if pilih_id in jenis_produk:
    jumlah_beli = int(input("Berapa jumlah barang yang akan dibeli: "))
    jumlah_bayar = jumlah_beli * daftar_harga[pilih_id]

    #Proses hitung jika pembeli mendapatkan diskon
    if jumlah_bayar > 5000000 :
        diskon = jumlah_bayar * 10 / 100
        jumlah_bayar = jumlah_bayar - diskon
        print(f"Selamat! anda mendapatkan diskon 10% dari pembelian produk")
    else:
        pass

    pilih_beli = input(f"Anda akan membeli produk {jenis_produk[pilih_id]} dengan jumlah {jumlah_beli}. Apakah anda yakin? (Y/N): ")
    if pilih_beli == "y" or pilih_beli == "Y":
        nama_pembeli    = input("Nama pembeli/penerima      : ")
        alamat_pembeli  = input("Alamat pembeli/penerima    : ")
        nomr_pembeli    = int(input("Nomor Hp pembeli/penerima  : "))
        print()

        print("=============================== Metode Pembayaran ===========================================")
        print()
        print("Silahkan pilih metode pembayaran yang anda inginkan")
        for i in metode_pembayaran:
            print("Id : ", i, "\t Metode Pembayaran : ", metode_pembayaran[i])
        print("=============================================================================================")
        print()
        pilih_metode = int(input("Pilih Id Metode Pembayaran (contoh 1, 2, 3): "))
        if pilih_metode in metode_pembayaran:
            konfirmasi = input(f"Anda memilih metode {metode_pembayaran[pilih_metode]}. Apakah anda yakin? (Y/N): ")
            if konfirmasi == "y" or konfirmasi == "Y":
                print()
                print("==================================== Struk Pembayaran =======================================")
                print()
                print("Nama Pembeli/Penerima        : ",nama_pembeli)
                print("Alamat Pembeli/Penerima      : ",alamat_pembeli)
                print("Nomor Hp Pembeli/Penerima    : ",nomr_pembeli)
                print("Jenis Product                : ",jenis_produk[pilih_id])
                print("Jumlah Dibeli                : ",jumlah_beli)
                print("Daftar Harga                 : ",daftar_harga[pilih_id])
                print("Total Pembayaran             : ",jumlah_bayar)
                print("Metode Pembayaran            : ",metode_pembayaran[pilih_metode])
                print("Pembayaran sudah di proses, terimakasih sudah berbelanja di toko kami :)")
                print("=============================================================================================")
            else:
                print("Mohon maaf jika terdapat kendala, silahkan ulangi transaksi")
        else:
            print("Maaf, metode pembayaran tidak tersedia")
    else:
        print("Jika ada yang salah atau anda belum yakin, anda bisa mengulangi pembelian :)")
else:
    print("Maaf, Id product tidak tersedia silahkan pilih kembali")

