import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    bracket_lst = list(map(str, input()))
    # print(bracket_lst)
    stack = []
    ans = 1
    for i in bracket_lst:
        try:
            if i == '(' or i == '{':
                stack.append(i)
            elif i == ')' or i == '}':
                if stack[-1] == '(' and i == ')':
                    stack.pop()
                elif stack[-1] == '{' and i == '}':
                    stack.pop()
                else:
                    break

        except:
            ans = 0
            break

    if stack:
        ans = 0

    print(f'#{tc} {ans}')