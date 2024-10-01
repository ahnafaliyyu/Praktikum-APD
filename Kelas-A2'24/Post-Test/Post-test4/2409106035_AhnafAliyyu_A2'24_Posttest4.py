kesempatan=3
while kesempatan > 0:
    username=input("Masukkan Username ")
    password=input("Masukkan Password ")

    if username=="ahnaf" and password=="35":
        print("Berhasil Login")
        break
    else:
        print("Username atau Password salah!")
        kesempatan-=1
        print(f"Kesempatan login tersisa {kesempatan} kali")


if kesempatan > 0:
    while True:
        nama = input ("masukkan nama: ")
        nim = input("masukkan nim: ")
        pinjaman = int(input("masukkan jumlah pinjaman: "))
        lama =int(input("masukkan lama cicilan (1-3): "))
        
        if  lama == 1:
            bunga = 0.07
            bulan = 12 
        elif lama == 2:
            bunga = 0.13
            bulan = 24
        elif lama == 3:
            bunga = 0.19 
            bulan = 36
        else :
            print("anda tidak memenuhi syarat input")
        bungaperbulan = (bunga / 12) * pinjaman
        total = (pinjaman + bungaperbulan) / bulan
        print (f"{nama} dengan nim {nim} ingin melakukan pinjaman sebesar Rp {pinjaman} dan total cicilan perbulannya  adalah Rp{total}")
        
        ulang = input("Apakah anda ingin mengulang lagi?")
        if ulang == "Ya" or "ya":
            continue
        else:
            break
