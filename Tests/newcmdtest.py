print("D.A.V.E.: Sir, for this action you will have to type at the shell.")
print("D.A.V.E.: Should I start?")
op = input('You: ')
if op == 'yes' or op == 'Yes' or op == 'y':
    file = open('tt.txt', 'a+')
    print("D.A.V.E.: Please, type the command keyword:")
    cmd_key = input('You: ')
    print("D.A.V.E.: Now type many ways to call this function and type s when you're finished:")
    cmd = None
    while cmd != 's':
        cmd = input('Type the command: ')
        if cmd == 's':
            file.writelines('\n' + cmd + '\t' + cmd_key)
    file.close()
elif op == 'no' or op == 'No' or op == 'n':
    print('Okay')
else:
    print("I couldn't understand.")
