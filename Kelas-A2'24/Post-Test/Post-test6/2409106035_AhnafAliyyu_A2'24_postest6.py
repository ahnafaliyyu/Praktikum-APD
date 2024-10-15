users = {
    "admin": {"password": "admin ganteng"},
    "user": {"password": "user biasa"},
}  

data_klub = {}

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
                    ==============================
                    |  Klub Bola Peserta Liga 1   |
                    ==============================
                    |    1. TAMBAH DATA           |
                    |    2. TAMPILKAN DATA        |
                    |    3. UBAH DATA             |
                    |    4. HAPUS DATA            |
                    |    5. KELUAR                |
                    ==============================
                    """
                )
                while True:
                    pilih = int(input("PILIH : "))
                    if pilih == 1:
                        klub = input("Klub : ")
                        value_market = input("Value Market : ")
                        daerah = input("Daerah : ")
                        pemilik = input("Pemilik: ")
                        data_klub[klub] = {
                            "value_market": value_market, 
                            "daerah": daerah, 
                            "pemilik": pemilik
                        }

                    elif pilih == 2:
                        if len(data_klub) == 0:
                            print("Data klub masih kosong.")
                        else:
                            for klub, info in data_klub.items():
                                print(f"\nKlub: {klub}\nValue Market: {info['value_market']}\nDaerah: {info['daerah']}\nPemilik: {info['pemilik']}")

                    elif pilih == 3:
                        klub_lama = input("Nama Klub yang akan diubah: ")
                        if klub_lama in data_klub:
                            klub_baru = input("Klub baru: ")
                            value_market_baru = input("Value Market baru: ")
                            daerah_baru = input("Daerah baru: ")
                            pemilik_baru = input("Pemilik baru: ")
                            data_klub[klub_baru] = {
                                "value_market": value_market_baru, 
                                "daerah": daerah_baru, 
                                "pemilik": pemilik_baru
                            }
                            if klub_baru != klub_lama:
                                del data_klub[klub_lama]
                            print(f"Data klub {klub_lama} berhasil diubah.")
                        else:
                            print("Klub tidak ditemukan.")
                    
                    elif pilih == 4:
                        klub_lama = input("Nama Klub yang ingin dihapus: ")
                        if klub_lama in data_klub:
                            del data_klub[klub_lama]
                            print(f"Klub {klub_lama} berhasil dihapus.")
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
                    ==============================
                    |  Klub Bola Peserta Liga 1   |
                    ==============================
                    |    1. TAMBAH DATA           |
                    |    2. TAMPILKAN DATA        |
                    |    3. KELUAR                |
                    ==============================
                    """
                )
                while True:
                    pilih = int(input("PILIH : "))
                    if pilih == 1:
                        klub = input("Klub : ")
                        value_market = input("Value Market : ")
                        daerah = input("Daerah : ")
                        pemilik = input("Pemilik: ")
                        data_klub[klub] = {
                            "value_market": value_market, 
                            "daerah": daerah, 
                            "pemilik": pemilik
                        }

                    elif pilih == 2: 
                        if len(data_klub) == 0:
                            print("Data klub masih kosong.")
                        else:
                            for klub, info in data_klub.items():
                                print(f"\nKlub: {klub}\nValue Market: {info['value_market']}\nDaerah: {info['daerah']}\nPemilik: {info['pemilik']}")

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
