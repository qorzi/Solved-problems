import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    while M:
        M -= 1
        tmp = lst.pop(0)
        lst.append(tmp)

    print(f'#{tc} {lst[0]}')