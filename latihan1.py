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
tanggal = input('Masukan tanggal 4 hari kedepan (yyyy-mm-dd): ' )

hasil = diffDate(tanggal)

print('Selisih tanggal {0} dengan sekarang adalah {1} hari'.format(tanggal,hasil))
