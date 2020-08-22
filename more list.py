barang = ['kunci','ember','jaket','ban','mobile']
print(barang)

# mengambil beberapa method yang bisa digunakan untuk memanipulasi list
# method menambah data dalam list
barang.append('sepeda')
print(barang)

barang.extend('dompet')
print(barang)

barang.insert(2,'mobil bmw')
print(barang)

jumlahSepeda = barang.count('sepeda')
print('Jumlah Sepeda adalah:',jumlahSepeda)

barang.remove('mobil bmw')
print(barang)

barang.reverse()
print(barang)

print(100*'=')

stuff = barang.copy()
stuff.append('gelas')
print(stuff)
print(barang)