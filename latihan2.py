from datetime import*

namaFile = open('d:\dataPinjam.txt', 'r')
namaFile2 = open('d:\dataPinjam.txt', 'a')

while True :
    kode = input('Masukan Kode Member : ')
    nama = input('Masukan Nama Member : ')
    judul = input('Masukan Judul Buku : ')
    skrng = datetime.date(datetime.now())
    besok = skrng + timedelta(days=7)
    namaFile2.write(kode + '|' + nama + '|' + judul + '|' + str(skrng) + '|' + str(besok) + '\n')
    
    tambah = input('\nMau lagi (y/n) : ')
    ('\n')
    if tambah == 'y':
        True
    elif tambah == 'n' :
        break
    else :
        print('Inputan invalid')
        break

namaFile2.close()
