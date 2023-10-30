pelanggan = "budi"
totalbelanja = 800000

#struktur kendali if
if(totalbelanja > 100000):
    keterangan ="selamat anda mendapat hadiah"
    
else:
    keterangan = "terimakasih"

print("pelanggan",pelanggan,"\nTotal belanja anda RP." , totalbelanja, "\n",keterangan)

nama ="budi"
matpel ="ipa"
nilai = 79.99

keterangan = "Lulus" if nilai >= 60 else "Gagal"
print("Nama siswa \t:",nama,
      "\nMata pelajaran \t:", matpel,
      "\nNilai \t\t:",nilai,
      "\nKeterangan \t:", keterangan)

nama ="budi"
matpel ="ipa"
nilai = 89.99

if(nilai >= 85 and nilai <= 100):
    grade = "A"
elif(nilai >= 75 and nilai <=85):
    grade = "B"
elif(nilai >= 60 and nilai <=70):
    grade ="C"
elif(nilai >= 40 and nilai <=50):
    grade ="D"
else:
    grade ="E"
print("Nama siswa \t:",nama,
      "\nMata pelajaran \t:", matpel,
      "\nNilai \t\t:",nilai,
      "\nGrade \t:", grade)
     

