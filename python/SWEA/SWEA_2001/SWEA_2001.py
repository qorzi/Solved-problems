import sys
sys.stdin = open("input (4).txt", "r")

T = int(input())

for j in range(1, T+1):
    N, M = map(int, input().split())
    A = []
    for i in range(0, N):
        A += [list(map(int, input().split()))]
    Y = []
    x = 0
    for a in range(0, N-M+1):
        for b in range(0, N-M+1):
            Y += [x]
            x = 0
            for c in range(0, M):
                for d in range(0, M):
                    x += A[a+c][b+d]

    print(f'#{j} {max(Y)}')