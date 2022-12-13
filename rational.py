x = 0
y = 0


def init(a, b):
    global x
    global y
    x = a
    y = b


def parse(data):
    try:
        return float(data)
    except ValueError:
        num, denom = data.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac


def sum():
    num_1 = parse(x)
    num_2 = parse(y)
    return num_1 + num_2


def sub():
    num_1 = parse(x)
    num_2 = parse(y)
    return num_1 - num_2


def div():
    num_1 = parse(x)
    num_2 = parse(y)
    return num_1 / num_2


def mult():
    num_1 = parse(x)
    num_2 = parse(y)
    return num_1 * num_2
