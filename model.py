import comp
import rational
TYPE_NUM = None


def init(a, b, type_num):
    global TYPE_NUM
    TYPE_NUM = type_num
    if type_num:
        comp.init(a, b)

    else:
        rational.init(a, b)


def mult():
    if TYPE_NUM:
        return comp.mult()
    else:
        return rational.mult()


def sub():
    if TYPE_NUM:
        return comp.sub()
    else:
        return rational.sub()


def sum():
    if TYPE_NUM:
        return comp.sum()
    else:
        return rational.sum()


def div():
    if TYPE_NUM:
        return comp.div()
    else:
        return rational.div()
