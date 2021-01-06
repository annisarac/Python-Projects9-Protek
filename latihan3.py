from datetime import*

def diffDate(x):
    tgl = x.split('-')
    listTgl = []

    for i in tgl:
        listTgl.append(int(i))

    tgl1 = date(listTgl[0], listTgl[1], listTgl[2])
    tgl2 = datetime.date(datetime.now())

    a = tgl1 - tgl2
    b = a.days
    return b

myFile = open('d:\dataPinjam.txt', 'r')
file = myFile.readlines()

cariKode = input('Masukan Kode Member yang di cari : ' )

for i in range(len(file)):
    if(cariKode in file[i]):
        data = file[i].split('|')
    else:
        print('Data Mahasiswa Tidak Ditemukan')
        continue
print('Data Peminjaman Buku')
print('Kode Member : ' , data[0])
print('Nama Member : ' , data[1])
print('Judul Buku : ' , data[2])
print('Tanggal Mulai Pinjam : ', data[3])
print('Tanggal Max Peminjaman : ', data[4])
print('Tanggal Pengembalian : ', datetime.date(datetime.today()))
terlambat = diffDate(data[4])
denda = 2000*abs(terlambat)
if(terlambat >= 0):
    print('Terlambat : 0 hari')
    print('Denda : 0')
else:
    print('Terlambat : ', abs(terlambat))
    print('Denda : ', denda)


