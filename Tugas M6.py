#No 1
Usia= int(input("Your age:"))
Dep=input("Your department:")
lolos= Usia >= 19 and "Statistika" in Dep
print("Status lolos asisten:",str(lolos))

#No 2
data_pelanggan=("Fikri","Premium")
nama,status_member=data_pelanggan
berat_kardus=[26,34,12,23,45,5]
VIP="Premium" in data_pelanggan or sum(berat_kardus)>=100
print("#No 2")
print(f"Pengriman jalur VIP: {VIP}")

#No 3
riwayat_nilai=[]
kategori_nilai=[]
IP1=float(input("Masukan IP 1:"))
IP2=float(input("Masukan IP 2:"))
IP3=float(input("Masukan IP 3:"))
riwayat_nilai.append(IP1)
riwayat_nilai.append(IP2)
riwayat_nilai.append(IP3)
for ip in riwayat_nilai:
    if ip == 4.0:
        kategori_nilai.append("A")
    elif ip >= 3.5 and ip <=3.99:
        kategori_nilai.append("AB")
    elif ip >= 3.0 and  ip <=3.49:
        kategori_nilai.append("B")
    elif ip >= 2.5 and ip <=2.99:
        kategori_nilai.append("BC")
    elif ip >= 2.0 and ip <= 2.49 :
        kategori_nilai.append("C")
    elif ip >= 1 and ip <=1.99:
        kategori_nilai.append("D")
    else:
        kategori_nilai.append("E")
        
IPK=sum(riwayat_nilai)/len(riwayat_nilai)
lolos_dokumen=IPK>=3.5 and "E" not in kategori_nilai
print('Status lolos dokumen:',lolos_dokumen)

