nama = input ("Masukkan Nama")
nim = input ("masukkan nim")
hargaberas = int(input("masukkan harga beras"))

diskon = {
    "diskon1":0.11,
    "diskon2":0.14,
    "diskon3":0.17
}

diskon_beras_mawar= hargaberas * diskon["diskon1"]
diskon_beras_sania= hargaberas * diskon["diskon2"]
diskon_beras_maknyus= hargaberas * diskon["diskon3"]

mawar = hargaberas - diskon_beras_mawar
sania = hargaberas - diskon_beras_sania
maknyus = hargaberas - diskon_beras_maknyus



print(f"{nama} dengan {nim} ingin membeli beras seharga {hargaberas}" "\n"
f"jika dia membeli beras mawar ia harus membayar seharga {mawar} setelah mendapat diskon 11%" "\n"
f"jika dia membeli beras sania ia harus membayar seharga {sania} setelah mendapat diskon 14%" "\n"
f"jika dia membeli beras maknyus ia harus membayar seharga {maknyus} setelah mendapat diskon 17%")