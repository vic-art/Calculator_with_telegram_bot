x = 0
y = 0


def init(a, b):
    global x
    global y
    x = a
    y = b


def parse(data):
    data = data.replace(" ", "")
    for n, x in enumerate(data):
        if x == "+" or x == "-":
            data_real = data[:n]
        elif x == "i":
            data_complex = data[len(data_real):len(data)-1]
    return float(data_real), float(data_complex)


def sum():
    list1 = parse(x)
    list2 = parse(y)
    real = list1[0] + list2[0]
    imag = list1[1] + list2[1]
    if imag < 0:
        return f'{real} - {imag*(-1)}*i'
    return f'{real} + {imag}*i'


def sub():
    list1 = parse(x)
    list2 = parse(y)
    real = list1[0] - list2[0]
    imag = list1[1] - list2[1]
    if imag < 0:
        return f'{real} - {imag*(-1)}*i'
    return f'{real} + {imag}*i'


def mult():
    list1 = parse(x)
    list2 = parse(y)
    real = list1[0] * list2[0] - list1[1] * list2[1]
    imag = list1[0] * list2[1] + list2[0] * list1[1]
    if imag < 0:
        return f'{real} - {imag*(-1)}*i'
    return f'{real} + {imag}*i'


def div():
    x = x.replace(" ", "").replace("i", "j")
    y = y.replace(" ", "").replace("i", "j")
    return complex(x) / complex(y)
