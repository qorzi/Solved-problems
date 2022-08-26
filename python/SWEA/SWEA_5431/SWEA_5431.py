import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    lst_all = [i for i in range(1, N+1)]

    for i in lst:
        lst_all.remove(i)

    print(f'#{tc}', *lst_all)