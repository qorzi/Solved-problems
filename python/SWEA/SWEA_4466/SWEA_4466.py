import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    lst.sort()
    sum_int = 0
    for _ in range(K):
        sum_int += lst.pop()

    print(f'#{tc} {sum_int}')