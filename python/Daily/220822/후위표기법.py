isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

T = int(input())
for tc in range(1, T+1):
    lst = list(map(str, input()))

    stack = []
    ans = []

    for i in lst:
        if i in nums:
            ans.append(i)
        elif i in isp:
            if i == '(':
                stack.append(i)
            elif i == '*' or i == '/':
                print(stack)
                while stack[-1] != '+' or stack[-1] != '-':
                    ans.append(stack.pop())
                stack.append(i)

            elif i == '+' or i == '-':
                stack += [i]
            elif i == ')':
                while stack[-1] != '(':
                    ans.append(stack.pop())
                stack.pop()

    for i in stack:
        ans += stack.pop()

    print(f'#{tc} {ans}')