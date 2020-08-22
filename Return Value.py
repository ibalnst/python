
def kuadrat(argumen):
    total = argumen**2
    print('Nilai kuadrat dari',argumen,'adalah:',total)
    return total


a = kuadrat(4)
print(a)

print('+'*100)

# fungsi dengan return value dan multiple argumen

def tambah(argumen1,argumen2):
    total = argumen1 + argumen2
    print(argumen1,'+',argumen2,'=',total)
    return total

def kali(argumen1,argumen2):
    total = argumen1 * argumen2
    print(argumen1,'x',argumen2,'=',total)
    return total


a = tambah(3,4)
b = kali(3,tambah(5,6))
print(a)
print(b)
