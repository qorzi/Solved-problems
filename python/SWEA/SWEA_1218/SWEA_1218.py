import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    lst_len = int(input())
    lst = list(map(str, input()))
    stack = []

    ans = 1
    for i in lst:
        try:
            # print(stack[-1], i)
            if i == '(' or i == '{' or i == '[' or i == '<':
                stack.append(i)
            elif stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack[-1] == '{' and i == '}':
                stack.pop()
            elif stack[-1] == '[' and i == ']':
                stack.pop()
            elif stack[-1] == '<' and i == '>':
                stack.pop()
            else:
                ans = 0
                break
        except:
            pass

    if stack:
        ans = 0

    print(f'#{tc} {ans}')