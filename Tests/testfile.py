
'''
file = open('name.txt', 'w')
#file.write('pedro')
file.close()
'''

keyname = ["my name is", "you can call me", "I am called"]

def get_name():
    result = None
    file = open('name.txt', 'r')
    result = file.read()
    file.close()
    return result

def change_name(text):
    result = None
    newname = None
    file = open('name.txt', 'w')
    for key in keyname:
        if text.startswith(key):
            newname = text.replace(key, '')
    file.write(newname)
    file.close()
    return None

while True:
    print('Your name is ' + get_name())
    nn = input("What's your new name: ")
    nn = str(nn)
    change_name(nn)
