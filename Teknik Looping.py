# Teknik Looping

nama_band = ['Payung Teduh','Fourtwnty','Dialog Dini Hari',
             'Mr. SOnjaya','Parahyena','Syahrini']

#iterasi = 1;
#for band in nama_band:
#    print('no:',iterasi,'Nama Band:',band)
#    iterasi+=1

listLagu = ['Akad',
        'Zona Nyaman',
        'Rumahku',
        'Sang Filsuf',
        'Sindoro','Jodohku']

#enumerate

for i,band in enumerate(nama_band):
    print('Nama Band',i,':',band)

#zip

for band,lagu in zip(nama_band,listLagu):
    print(band,'akan menyanyikan lagu yang berjudul:',lagu)

#set

playlist = {'babybaby','ada apa dengan cinta','cenat-cenut'
            ,'jaran Goyang'}

for lagulagu in sorted(playlist):
    print(lagulagu)
for lagulagu in playlist:
    print(lagulagu)


#dictionary
print('='*50)


playlist2 = {'Payung Teduh':'Akad',
             'Fourtwnty':'Zona Nyaman',
             'Dialog DIni Hari':'rumahku'
             }
for z,c in playlist2.items():
    print(z,'lagunya',c)

for i in reversed(range(1,10,1)):
    print(i)