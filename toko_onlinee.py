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
print("Toko kami terletak di Jl. Prawisata, Desa Toya, Kec. Aikmel, Kab. Lombok Timur")
print()
#perulangan untuk menampilkan produk dan daftar harganya
for i in jenis_produk :
    print("Id Product : ",i,"\t Nama Product : ",jenis_produk[i],"\t Harga Product : Rp",daftar_harga[i])
print("Pembelian diatas Rp5000000 akan mendapatkan diskon 10%")
print("=============================================================================================")
print("=============================================================================================")
print("=============================================================================================")
print()

#proses pemilihan produk yang ingin di beli
pilih_produk = int(input("Silahkan pilih produk yang anda inginkan. (contoh 1, 2, 3 dst.): "))
if pilih_produk in jenis_produk :
    jumlah_beli = int(input("Berapa jumlah barang yang akan dibeli: "))
    jumlah_bayar = jumlah_beli * daftar_harga[pilih_produk]

    #proses hitung jika pembeli mendapatkan diskon
    if jumlah_bayar > 5000000:
        diskon = jumlah_bayar * 10 / 100
        jumlah_bayar = jumlah_bayar - diskon
        print(f"Selamat! anda mendapatkan diskon 10% dari pembelian produk")
    else:
        pass

    #konfirmasi pilihan produk    
    pilih_beli = input(f"Anda memilih produk {jenis_produk[pilih_produk]} dengan jumlah {jumlah_beli}. Apakah anda yakin? (Y/N): ")
    if pilih_beli == "y" or pilih_beli == "Y" :
        nama_pembeli    = input("Nama Pembeli/Penerima          : ")
        alamat_pembeli  = input("Alamat Pembeli/Penerima        : ")
        nomr_pembeli    = int(input("Nomor Hp Pembeli/Penerima      : "))
        
        #konfirmasi data diri
        konfirmasi1 = input(f"Konfirmasi data diri, nama pembeli/penerima {nama_pembeli}, alamat {alamat_pembeli}, nomor Hp {nomr_pembeli}. Apakah sudah benar? (Y/N): ")
        print()
        print("=============================== Metode Pembayaran ===========================================")
        if konfirmasi1 == "y" or konfirmasi1 == "Y":
            #perulangan untuk menampilkan metode pembayaran produk
            for i in metode_pembayaran :
                 print("Id : ", i, "\t Metode Pembayaran : ", metode_pembayaran[i])
            print("=============================================================================================")
            print()
            #proses pemilihan metode pembayaran
            pilih_metode = int(input("Pilih Id Metode Pembayaran (contoh 1, 2, 3): "))
            if pilih_metode in metode_pembayaran :
                #konfirmasi pilihan metode pembayaran
                konfirmasi3 = input(f"Anda memilih metode {metode_pembayaran[pilih_metode]}. Apakah anda yakin? (Y/N): ")
                if konfirmasi3 == "y" or konfirmasi3 == "Y" :
                   if pilih_metode == 1 :
                       nomr_rekening = int(input("Silahkan masukkan nomor rekening anda: "))
                       print()
                       print("==================================== Struk Pembayaran =======================================")
                       print("Nama Pembeli/Penerima        : ",nama_pembeli)
                       print("Alamat Pembeli/Penerima      : ",alamat_pembeli)
                       print("Nomor Hp Pembeli/Penerima    : ",nomr_pembeli)
                       print("Jenis Product                : ",jenis_produk[pilih_produk])
                       print("Jumlah Dibeli                : ",jumlah_beli)
                       print("Daftar Harga                 : ",daftar_harga[pilih_produk])
                       print("Total Pembayaran             : ",jumlah_bayar)
                       print("Metode Pembayaran            : ",metode_pembayaran[pilih_metode])
                       print("Nomor Rekening               : ",nomr_rekening)
                       print("Terimakasih sudah berbelanja di toko kami, kami harap anda senang dengan pelayanan kami")
                       print("=============================================================================================")
                   else:
                       print()
                       print("==================================== Struk Pembayaran =======================================")
                       print("Nama Pembeli/Penerima        : ",nama_pembeli)
                       print("Alamat Pembeli/Penerima      : ",alamat_pembeli)
                       print("Nomor Hp Pembeli/Penerima    : ",nomr_pembeli)
                       print("Jenis Product                : ",jenis_produk[pilih_produk])
                       print("Jumlah Dibeli                : ",jumlah_beli)
                       print("Daftar Harga                 : ",daftar_harga[pilih_produk])
                       print("Total Pembayaran             : ",jumlah_bayar)
                       print("Metode Pembayaran            : ",metode_pembayaran[pilih_metode])
                       print("Terimakasih sudah berbelanja di toko kami, kami harap anda senang dengan pelayanan kami")
                       print("=============================================================================================")
                else:
                    print("Jika masih ada yang salah, anda dapat mengulangi kembali")
            else:
                print("Maaf, Id pembayaran tidak tersedia. Silahkan pilih kembali")
        else:
            print("Jika ada yang salah dengan data diri anda terkait nama, alamat ataupun nomor hp, silahkan ulangi pembelian dan pastikan data sudah benar!")
    else:
        print("Jika ada yang salah atau anda belum yakin, anda bisa mengulangi pembelian")
else:
    print("Maaf, Id produk tidak tersedia. Silahkan pilih kekmbali")