nama = input ("masukkan nama: ")
nim = input("masukkan nim: ")
x = int(input("masukkan jumlah pinjaman: "))
y =int(input("masukkan lama cicilan (1-3): "))
 
if  y == 1:
    z = 0.07
    b = 12
elif y == 2:
    z = 0.13
    b = 24
elif y == 3:
    z = 0.19
    b = 36
else :
    print("anda tidak memenuhi syarat input")

 
a = (z / 12) * x
total = (x + a) / b
print (f"{nama} dengan nim {nim} ingin melakukan pinjaman sebesar Rp {x} dan total cicilan perbulannya  adalah Rp{total}")