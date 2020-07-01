from mathop import op_add, op_minus, op_divide, op_cos, op_tan, op_sin

while True:
    s = input('Say the operation: ')
    s = s.split()


    if 'mais' in s:
        ans = op_add(s)
        print(ans)
    elif 'menos' in s:
        ans = op_minus(s)
        print(ans)
    elif 'vezes' in s:
        ans = op_times(s)
        print(ans)
    elif 'dividido' in s:
        ans = op_divide(s)
        print(ans)
    elif 'cosseno' in s:
        ans = op_cos(s)
        print(ans)
    elif 'seno' in s:
        ans = op_sin(s)
        print(ans)
    elif 'tangente' in s:
        ans = op_tan(s)
        print(ans)
    else:
        print('Operação mal realizada')
