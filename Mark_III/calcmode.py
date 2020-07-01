import math

def op_add(s):
    a = float(s[0])
    b = float(s[-1])
    ans = a + b
    return ans

def op_minus(s):
    a = float(s[0])
    b = float(s[-1])
    ans = a - b
    return ans

def op_times(s):
    a = float(s[0])
    b = float(s[-1])
    ans = a * b
    return ans

def op_divide(s):
    a = float(s[0])
    b = float(s[-1])
    ans = a / b
    return ans

def op_sin(s):
    b = float(s[-1])
    ans = math.sin(b)
    return ans

def op_cos(s):
    b = float(s[-1])
    ans = math.cos(b)
    return ans
def op_tan(s):
    b = float(s[-1])
    ans = math.tan(b)
    return ans

def calc_mode(x):
    s = x.split()

    if 'plus' in s:
        ans = op_add(s)
    elif 'minus' in s:
        ans = op_minus(s)
    elif 'times' in s:
        ans = op_times(s)
    elif 'divided' in s:
        ans = op_divide(s)
    elif 'cosine' in s:
        ans = op_cos(s)
    elif 'sine' in s:
        ans = op_sin(s)
    elif 'tangent' in s:
        ans = op_tan(s)
    else:
        ans = "I am sorry, but I couldn't understand"
    return ans

