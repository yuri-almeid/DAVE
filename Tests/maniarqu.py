'''
mf = open('tt.txt', 'r')
escrito = mf.read()
mf.close()
print(escrito)

while True:
    add = input('> ')
    file = open('tt.txt', 'r+')
    es = file.read()
    es = es + '\n' + add
    file.write(es)

    ler = file.readlines()
    print(ler)
    file.close()
'''
'''
def addfile(texto):
    arq = open('tt.txt', 'a+')
    arq.writelines('\n' + texto)
    arq.close()

def lefile():
    arq = open('tt.txt', 'r+')
    print('\n' + arq.read())
    arq.close()
'''
while True:
    ds1 = input('1> ')
    ds2 = input('2> ')
    ds = ds1 + '\t' + ds2
    addfile(ds)
    lefile()
