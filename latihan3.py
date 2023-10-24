#input nilai variabel
a=input("masukan nilai a=")
b=input("masukan nilai b=")

#cetak nilai variabel
print("variabel a=",a)
print("variabel b=",b)

#cetak hasil operasi kedua variabel dengan string format
print("hasil pengganbungan {0}+{1}=".format (a,b)+(a+b))

#konversinilai variabel
a=int(a)
b=int(b)
print("hasil perjualan {1}+{0}=%d".format (a,b) %(a+b))
print("hasil penjualan {1}/{0}=%d".format(a,b) %(a/b))