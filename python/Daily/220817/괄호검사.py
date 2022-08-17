import sys
sys.stdin = open('input_괄호검사.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    bracket_lst = list(map(str, input()))
    print(bracket_lst)
    stack = []
    ans = 1
    for i in bracket_lst:
        try:
            if i == '(':
                stack.append(i)
            elif i == ')':
                stack.pop()
        except:
            ans = -1
    if stack:
        ans = -1

    print(f'#{tc} {ans}')


