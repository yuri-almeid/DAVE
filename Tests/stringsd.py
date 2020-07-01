

# Teste de operações basicas
while True:

    s = input('Say the operation: ')
    s = str(s)

    if str(s.split(' ')[1]) == 'dividido':
        operation = 'dividido por'
        a = float(s.split(' ')[0])
        b = float(s.split(' ')[3])
    else:
        operation = str(s.split(' ')[1])
        a = float(s.split(' ')[0])
        b = float(s.split(' ')[2])
    ans = None
    if operation == 'mais':
        ans = a + b
        print(ans)
        
    elif operation == 'menos':
        ans = a - b
        print(ans)
        
    elif operation == 'dividido por':
        ans = a/b
        print(ans)

    elif operation == 'vezes':
        ans = a * b
        print(ans)
        

