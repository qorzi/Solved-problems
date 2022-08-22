def icp(a):
    if a == '(':
        return 3
    elif a == '*':
        return 2
    elif a == '+':
        return 1


def isp(a):
    if a == '(':
        return 0
    elif a == '*':
        return 2
    elif a == '+':
        return 1


for tc in range(1, 11):
    _ = input()
    formula = input()
    num = []
    op = []
    for alpha in formula:
        if alpha.isdecimal():
            num.append(alpha)
        else:
            if alpha == ")":
                while op[-1] != "(":
                    num.append(op.pop())
                op.pop()
            elif not op or icp(alpha) > isp(op[-1]):
                op.append(alpha)
            else:
                while op and icp(alpha) <= isp(op[-1]):
                    num.append(op.pop())
                op.append(alpha)
    while op:
        num.append(op.pop())

    stack = []
    for alpha in num:
        if alpha == '+':
            stack.append(stack.pop()+stack.pop())
        elif alpha == '*':
            stack.append(stack.pop()*stack.pop())
        else:
            stack.append(int(alpha))
    print(f"#{tc} {stack[-1]}")