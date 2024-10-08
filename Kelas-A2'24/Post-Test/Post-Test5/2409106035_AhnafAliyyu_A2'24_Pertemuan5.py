users = {
    "admin": {"password": "admin ganteng"},
    "user": {"password": "user biasa"},
}  

data_klub = []  

while True:
    print("Pilih opsi:")
    print("1. Register") 
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == '1': 
        username = input("Buat username: ")
        password = input("Buat password: ")
        if username in users:
            print("Username sudah ada, coba yang lain!")
        else:
            users[username] = {"password": password}
            print(f"Pengguna {username} berhasil didaftarkan!")

    elif pilihan == '2': 
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in users and users[username]["password"] == password:
            print(f"Login berhasil! Selamat datang, {username}")
            
            if username == "admin": 
                print(
                    """
                    =============================
                    |  Klub Bola Peserta Liga 1  |
                    =============================
                    |    1. TAMBAH DATA          |
                    |    2. TAMPILKAN DATA       |
                    |    3. UBAH DATA            |
                    |    4. HAPUS DATA           |
                    |    5. KELUAR               |
                    =============================
                    """
                )
                while True:
                    pilih = int(input("PILIH : "))
                    if pilih == 1: 
                        klub = input("Klub : ")
                        value_market = input("Value Market : ")
                        daerah = input("Daerah : ")
                        pemilik = input("Pemilik: ")
                        data_klub.append([klub, value_market, daerah, pemilik])

                    elif pilih == 2:  
                        if len(data_klub) == 0:
                            print("Data klub masih kosong.")
                        else:
                            for i in range(len(data_klub)):
                                print(f"\nData Klub ke-{i+1}\nKlub : {data_klub[i][0]}\nValue Market : {data_klub[i][1]}\nDaerah : {data_klub[i][2]}\nPemilik: {data_klub[i][3]}")
                    
                    elif pilih == 3:
                        klub_lama = input("Nama Klub yang akan diubah: ")
                        for i in range(len(data_klub)):
                            if data_klub[i][0] == klub_lama:
                                klub_baru = input("Klub : ")
                                value_market_baru = input("Value Market : ")
                                daerah_baru = input("Daerah : ")
                                pemilik_baru = input("Pemilik: ")
                                data_klub[i] = [klub_baru, value_market_baru, daerah_baru, pemilik_baru]
                                print(f"Data klub {klub_lama} berhasil diubah.")
                                break
                        else:
                            print("Klub tidak ditemukan.")
                    
                    elif pilih == 4: 
                        klub_lama = input("Nama Klub yang ingin dihapus: ")
                        for i in range(len(data_klub)):
                            if data_klub[i][0] == klub_lama:
                                del data_klub[i]
                                print(f"Klub {klub_lama} berhasil dihapus.")
                                break
                        else:
                            print("Klub tidak ditemukan.")
                    
                    elif pilih == 5:  
                        print("Terima kasih, kembali ke menu login.")
                        break
                    
                    else:
                        print("Pilihan tidak valid!")
            
            else: 
                print(
                    """
                    =============================
                    |  Klub Bola Peserta Liga 1  |
                    =============================
                    |    1. TAMBAH DATA          |
                    |    2. TAMPILKAN DATA       |
                    |    3. KELUAR               |
                    =============================
                    """
                )
                while True:
                    pilih = int(input("PILIH : "))
                    if pilih == 1: 
                        klub = input("Klub : ")
                        value_market = input("Value Market : ")
                        daerah = input("Daerah : ")
                        pemilik = input("Pemilik: ")
                        data_klub.append([klub, value_market, daerah, pemilik])

                    elif pilih == 2: 
                        if len(data_klub) == 0:
                            print("Data klub masih kosong.")
                        else:
                            for i in range(len(data_klub)):
                                print(f"\nData Klub ke-{i+1}\nKlub : {data_klub[i][0]}\nValue Market : {data_klub[i][1]}\nDaerah : {data_klub[i][2]}\nPemilik: {data_klub[i][3]}")
                    
                    elif pilih == 3:
                        print("Terima kasih, kembali ke menu login.")
                        break
                    
                    else:
                        print("Pilihan tidak valid!")

        else:
            print("Login gagal! Username atau password salah.")
    
    elif pilihan == '3': 
        print("Terima kasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak valid, coba lagi!")
