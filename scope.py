# scope variable : local & global

namaKucing = 'Liqui'
makananKuding = 'Royal Canin'

def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru # variabel global
    nama = namaBaru # variabel local
    print('saya rubah nama kucing menjadi',namaKucing)

def kasihMakanKucing(makanan,nama):
    global namaKucing,makananKucing
    namaKucing = nama
    makananKucing = makanan


rubahNamaKucing('Katie')
kasihMakanKucing('meo','puca')
print('nama kucing saya menjadi',namaKucing,'dan makan',makananKucing)