import sys
sys.stdin = open("input (4).txt", "r")

T = int(input())

for l in range(1, T+1):

    N, K = map(int, input().split())

    H = []
    for _ in range(0, N):
        H += [list(map(int, input().split()))]

    V = []
    for i in range(0, N):
        A = []
        for j in range(0, N):
            A += [H[j][i]]
        V += [A]

    M = [H, V]

    tvalue = 0
    for k in M:
        for i in range(0, N):
            B = k[i]
            B.append(0)
            B.insert(0, 0)
            tn = 0
            for j in range(1, N+1):
                if B[j] == 1:
                    if B[j-1] == 1 or B[j+1] == 1:
                        tn += 1
                    if j == N and tn == K:
                        tvalue += 1
                        tn = 0
                elif B[j] == 0:
                    if tn == K:
                        tvalue += 1
                    tn = 0
    print(f'#{l} {tvalue}')