print('\t\t\t\t\t\t\t======================')
print('\t\t\t\t\t\t\tAPOTIK NO DROP RIKLONA')
print('\t\t\t\t\t\t\t======================')
print()
print('APOTIK SAYA MENYEDIAKAN:')
print('\t\t\t\t\t\t\t1.RIKLONA   1 KOTAK  : 2.500.000,-')
print('\t\t\t\t\t\t\t2.DUMOLID   1 KOTAK  : 3.250.000,-')
print('\t\t\t\t\t\t\t3.ESTAZOLAM 1 KOTAK  : 2.225.000,-')
print('\t\t\t\t\t\t\t4.MERLOPAM  1 KOTAK  : 1.750.000,-')
print('\t\t\t\t\t\t\t5.XANAX     1 KOTAK  : 4.500.000,-')
print()
print('HARGA DISKON DENGAN PEMBELIAN SEBAGAI BERIKUT:')
print('\t\t\t\t\t\t\t1.PEMBELIAN DIATAS 10 JUTA MENDAPATKAN DISKON 15%')
print('\t\t\t\t\t\t\t2.PEMBELIAN 5 - 7 JUTA MENDAPATKAN DISKON 10%')
print('\t\t\t\t\t\t\t1.PEMBELIAN 2 - 5 JUTA MENDAPATKAN DISKON 5%')
print()
pilihan = int(input("PILIH PAKET 1-2-3-4-5 ? :\n"))

if pilihan == 1:
    hargaObat = 2500000
elif pilihan == 2:
    hargaObat = 3250000
elif pilihan == 3:
    hargaObat = 2225000
elif pilihan == 4:
    hargaObat = 1750000
elif pilihan == 5:
    hargaObat = 4500000
else:
    print()
    print('Pilihan anda tidak tersedia')
    print('Atas nama Apotik No Drop saya ucapkan terima kasih')

jumlah = int(input('Berapa kotak yang mau dibeli ? :\n'))

totalBelanja = jumlah * hargaObat

if totalBelanja >= 10000000:
    diskon = 15
elif totalBelanja >= 5000100 and totalBelanja <= 7000000:
    diskon = 10
elif totalBelanja >= 2000000 and totalBelanja <= 5000000:
    diskon = 5
else:
    diskon = 0

jumlahDiskon = totalBelanja * diskon / 100
hargaTotal = totalBelanja - jumlahDiskon

print()
print('\t\t\t\t\t\t\tJUMLAH BELANJA ANDA ADALAH')
print('\t\t\t\t\t\t\t==========================')
print()
print('\t\t\t\t\t\t\tPILIHAN PAKET      :', pilihan)
print('\t\t\t\t\t\t\tHARGA PERKOTAK     :', hargaObat)
print('\t\t\t\t\t\t\tJUMLAH PEMBELIAN   :', jumlah)
print('\t\t\t\t\t\t\tTOTAL BELANJA      : Rp.',totalBelanja)
print('\t\t\t\t\t\t\tDISKON             :', diskon)
print('\t\t\t\t\t\t\tJUMLAH DISKON      :', jumlahDiskon)
print('\t\t\t\t\t\t\t------------------------------')
print('\t\t\t\t\t\t\tTOTAL KESELURUHAN  :', hargaTotal)

print()
print('TERIMA KASIH SELAMAT SELAMAT BERBELANJA LAGI')
print('SALAM SATU BOTI')
