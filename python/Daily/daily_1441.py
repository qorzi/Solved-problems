def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    try:
        x/y
        return x / y
    except:
        print("'0'으로는 나눌 수 없습니다.")
