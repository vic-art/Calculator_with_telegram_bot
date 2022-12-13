import model


def type_of_number(a, b):
    if "i" in a and "i" in b:
        print('complex')
        model.init(a, b, True)  # if True -> the number is complex

    elif a.replace(",", "").replace(".", "").replace("/", "").isdigit() and \
            b.replace(",", "").replace(".", "").replace("/", "").isdigit():
        print('rational')

        model.init(a, b, False)  # if False -> the number is rational

    else:
        return ("Неправильный ввод. Введите комплексное или рациональное число.")
    return True


def type_of_operation(op):
    if "+" in op:
        result = model.sum()

    elif "-" in op:
        result = model.sub()

    elif "*" in op:
        result = model.mult()

    elif "/" in op:
        result = model.div()
    else:
        print("Оператор выбран неправильно")
    return result


def log(data):
    with open('log.txt', 'w') as f:
        f.write(str(data))


def view(data):
    print(data)


def run(num_1, num_2, op):
    if type_of_number(num_1, num_2):
        result = type_of_operation(op)
    else:
        result = False
    log(result)
    view(result)
    return result
