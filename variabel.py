kendaraan = ["mio","motor bebek","110 cc","warna biru","roda 2"]
kendaraan.append("16jt")
kendaraan.append("matic")
kendaraan.insert(1,"yamaha")
print(kendaraan)

soal = int (input("Menghitung Luas Bangun Datar (pilih dari 1-3) :"))
match soal:
    case 1:
        print("Menghitung Luas Persegi")
        sisiPersegi = int(input("Masukan sisi :"))
        luasPersegi = sisiPersegi * sisiPersegi
        print("Luas Persegi = " , luasPersegi)
    case 2:
        print("Menghitung Luas Lingkaran")
        jarijariLingkaran = int(input("masukan jarijari Lingkaran :"))
        luaslingkaran = 3.14 * jarijariLingkaran * jarijariLingkaran
        print("Luas Lingkaran = " , float(luaslingkaran))
    case 3:
        print("Menghitung Luas Segitiga")
        alasSegitiga = int(input("masukan Alas Segitiga :"))
        tinggiSegitiga = int(input("masukan Tinggi Segitiga :"))
        luasSegitiga = 1/2 * alasSegitiga * tinggiSegitiga
        print("Luas Segitiga = " , int(luasSegitiga))







