nama ="lee"
umur =18

if(umur <= 17):
    kategori ="anak-anak"
elif(umur >=18 and umur <=65):
    kategori ="dewasa"
elif(umur >=65 and umur <=90):
    kategori ="lanjut usia"

print("Nama \t:",nama,
      "\nUmur \t\t:",umur,
      "\nKategori \t:", kategori)

bil1 = 17
bil2 = 13

if(bil1 > bil2):
    hasil ="bil1 lebih besar dari bil2"
elif(bil1 < bil2):
    hasil= "bil2 lebih kecil dari bil1"

print( "\nHasil \t:", hasil)
    