from file_type import *

while True:
    i1 = input('1> ')
    i2 = input('2> ')

    ii = i1 + '\t' + i2

    addfile(ii, 'tt')
    readfile('tt')
