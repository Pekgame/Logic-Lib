one = True
zero = False

def AND(a: bool, b: bool) -> bool:
    return bool(a and b)

def NAND(a: bool, b: bool) -> bool:
    return not (a and b)

def OR(*args: bool):
    for arg in args:
        if arg:
            return True
    return False

def NOR(*args):
    for arg in args:
        if arg:
            return False
    return True

def XOR(a, b):
    return a != b

def XNOR(a, b):
    return a == b
