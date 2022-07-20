import sys
sys.stdin = open("input (4).txt", "r")

T = int(input())

for i in range(1, T+1):
    M = int(input())
    N = list(map(int, input().split()))
    y = 0
    a = max(N)
    print(f'first max: {a}')
    for j in range(0, M-1):
        x = N[j]
        if x == a:
            a = max(N[j+1::])
            print(f'max changed: {a}')
        if x <= a:
            y += a-x
    print(f'#{i} {y}')