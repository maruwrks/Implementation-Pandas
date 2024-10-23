import pandas as pd
import json

def isibarang(n):
    '''
    with open('Barang.txt', 'w') as f:
    
        for _ in range(n):
            kode = input('Kode: ')
            nama = input('Nama: ')
            jenis = input('jenis: ')
            jmlhbeli = input('Jumlah beli: ')
            hargaBeli = input('Harga beli: ')
            sisa = input('Sisa: ')
            untung = input('untung: ')

        f.write('{"kode":"'+kode+'", "Nama": "'+nama+'", "jenis": "'+jenis+'", "jmlhbeli": "'+jmlhbeli+'", "hargaBeli": "'+hargaBeli+'", "sisa": "'+sisa+'", "Untung": "'+untung+'"}\n')
    '''
    data = [
            {"kode":"S01", "Nama": "Lux", "jenis": "sabun", "jmlhbeli": "10", "hargaBeli": "1000"},
            {"kode":"S02", "Nama": "Rinso", "jenis": "sabun", "jmlhbeli": "20", "hargaBeli": "1500"},
            {"kode": "M01", "Nama": "Kacang", "jenis": "makanan", "jmlhbeli": "25", "hargaBeli": "500"},
            {"kode": "S03", "Nama": "Mamalime", "jenis": "sabun", "jmlhbeli": "20", "hargaBeli": "1250"},
            {"kode": "M02", "Nama": "Fanta", "jenis": "makanan", "jmlhbeli": "15", "hargaBeli": "2000"},
            {"kode": "P01", "Nama": "Ember", "jenis": "plastik", "jmlhbeli": "10", "hargaBeli": "10000"}
            ]
    with open('Barang.txt', 'w') as f:
        for i in data:
            f.write(json.dumps(i) + '\n')
n = int(input('Masukkan jumlah barang: '))
isibarang(n)

def isijual(n):
    '''
    with open('jual.txt', 'w') as f:
        for _ in range(n):
            tanggal = input('Tanggal: ')
            kode = input('Kode: ')
            jumlah = input('Jumlah: ')
            harga = input('Harga: ')
            potongan = input('potongan: ')
            f.write('{"tanggal": "'+tanggal+'","kode":"'+kode+'", "jumlah": "'+jumlah+'", "harga": "'+harga+'", "potongan": "'+potongan+'"}\n')
    '''
    jual = [
            {"tanggal": "01-01-18", "kode": "S01", "jumlah": "3", "harga": "1200", "potongan": "5"},
            {"tanggal": "01-01-18", "kode": "M01", "jumlah": "2", "harga": "750", "potongan": "10"},
            {"tanggal": "01-01-18", "kode": "S03", "jumlah": "1", "harga": "1500", "potongan": "0"},
            {"tanggal": "01-01-18", "kode": "M02", "jumlah": "1", "harga": "2500", "potongan": "0"},
            {"tanggal": "01-01-18", "kode": "S01", "jumlah": "2", "harga": "1200", "potongan": "0"},
            {"tanggal": "02-01-18", "kode": "S02", "jumlah": "1", "harga": "2000", "potongan": "0"},
            {"tanggal": "02-01-18", "kode": "M02", "jumlah": "5", "harga": "2250", "potongan": "0"},
            {"tanggal": "02-01-18", "kode": "P01", "jumlah": "1", "harga": "15000", "potongan": "25"},
            {"tanggal": "03-01-18", "kode": "S01", "jumlah": "5", "harga": "1500", "potongan": "10"},
            {"tanggal": "03-01-18", "kode": "P01", "jumlah": "1", "harga": "15000", "potongan": "10"},
            ]
    with open('jual.txt', 'w') as f:
        for i in jual:
            f.write(json.dumps(i) + '\n')
n = int(input('Masukkan penjualan: '))
isijual(n)

def Dataframe(mode):
        if mode == 'a':
            dfbrg = pd.read_json('Barang.txt', lines=True)
            print(f'\n{dfbrg}\n')
        elif mode == 'b':
            dfjual = pd.read_json('jual.txt', lines=True)
            print(f'{dfjual}\n')
for _ in range(2):  
    mode = input('Masukkan pilihan mode (a untuk Barang, b untuk Jual): ')
    Dataframe(mode)

dfbrg = pd.read_json('Barang.txt', lines=True)
dfjual = pd.read_json('jual.txt', lines=True)

def Hitungsisa(dfbrg, dfjual):
    jualUnik = dfjual['kode'].unique()
    brgUnik = dfbrg['kode'].unique()
    for jual in jualUnik:
        jml = 0
        hasil = 0
        dataBrg = dfjual[dfjual['kode'] == jual]
        for _, row in dataBrg.iterrows():
            jml += row['jumlah']
            beli = dfbrg.loc[dfbrg['kode'] == jual, 'jmlhbeli']
            hasil += (row['harga'] * ((100 - row['potongan']) / 100) - dfbrg.loc[dfbrg['kode'] == jual, 'hargaBeli']) * row['jumlah']
        if jml != 0:
            dfbrg.loc[dfbrg['kode'] == jual, 'sisa'] = beli - jml
            dfbrg.loc[dfbrg['kode'] == jual, 'Untung'] = hasil
    for barang in brgUnik:
        if barang not in jualUnik:
            dfbrg.loc[dfbrg['kode'] == barang, 'sisa'] = dfbrg['jmlhbeli']
            dfbrg.loc[dfbrg['kode'] == barang, 'untung'] = 0
    with open("Barang.txt", "w") as file:
        line = dfbrg.to_string(index=False) + "\n"
        file.write(line)
    with open("Barang.txt", "r") as file:
        isi = file.read()
        print(f'Isi file Barang.txt setelah ditambah Nilai Total :\n{isi}')

Hitungsisa(dfbrg, dfjual)
print(f'{dfbrg}\n')


def Urutjenis(dfbrg):
    dfbrg=dfbrg.sort_values(by='jenis', ascending=True)
    print(f'data setelah di urutkan: \n {dfbrg}\n')
Urutjenis(dfbrg)

def laporan(dfbrg) :
    keuntungan = dfbrg.groupby('jenis')['Untung'].sum().reset_index() 
    total = dfbrg['Untung'].sum() 
    report = f'keuntungan berdasarkan jenis \n{keuntungan}\n'
    report += f"total keuntungan : {total}"
    with open("laporan.txt", "w") as f:
        f.write(report)
    with open("laporan.txt", "r") as f:
        baca = f.read()
        print("Isi file laporan :")
        print(baca)
laporan(dfbrg)

def Tambahbar(dfbrg):
    n = int(input('Masukkan jumlah barang di tambah : '))
    data = []
    for i in range(n):
        kode = input('Kode: ')
        nama = input('Nama: ')
        jenis = input('jenis: ')
        jmlhbeli = int(input('Jumlah beli: '))  
        hargaBeli = int(input('Harga beli: '))  
        sisa = jmlhbeli
        untung = 0
        tambah = {'kode': kode, 'Nama': nama, 'jenis': jenis, 'jmlhbeli': jmlhbeli, 'hargaBeli': hargaBeli, 'sisa': sisa, 'Untung': untung}
        data.append(tambah)
    df = pd.DataFrame(data)
    dfbrg = pd.concat([dfbrg, df], ignore_index=True)
    dfbrg.to_json('Barang.txt', orient='records', lines=True)
    return dfbrg
dfbrg = Tambahbar(dfbrg)
print(dfbrg)

def Edit(dfbrg,edit, **kwargs ):
        if 'kode' in kwargs:
            kode = kwargs['kode']
            i = int(input("berapa data yang ingin diubah: "))
            for _ in range(i):
                ubah = input("Masukkan data yang ingin diubah: ")
                if ubah in dfbrg.columns:
                    diubah = input("Diubah menjadi: ")
                    if ubah == 'jml_beli' or ubah == 'hargabeli':
                        diubah = int (diubah)
                    dfbrg.loc[dfbrg['kode']==kode, ubah]= diubah

        with open("Barang.txt","w") as file: 
            line = dfbrg.to_string(index = False) + '\n'
            file.write(line)
        return dfbrg
edit = input("masukkan kode data yang ingin diubah: ")
dfbrg = Edit(dfbrg, edit, kode = edit)
print(dfbrg)

def revisi(dfbrg):
    indeks = dfbrg[dfbrg['sisa'] < 1].index
    dfbrg = dfbrg.drop(indeks)
    with open("Revisi.txt", "w") as file:
        file.write(dfbrg.to_string(index=False) + '\n')
    with open("Revisi.txt", "r") as file:
        isi = file.read()
        print(f'isi file revisi:\n{isi}')
revisi(dfbrg)

