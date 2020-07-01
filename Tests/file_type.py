# Função que escreve em arquivo
def addfile(text, name):
    file_name = name + '.txt'
    file = open(file_name, 'a+')
    file.writelines('\n' + text)
    file.close()

# Função que lê arquivo
def readfile(name):
    file_name = name + '.txt'
    arq = open(file_name, 'r+')
    print('\n' + arq.read())
    arq.close()
