import sys
sys.stdin = open("input (3).txt", "r")

Z = int(input())

for i in range(1, Z+1):
    M, N = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if M < N:
        M, N = N, M
        A, B = B, A

    for _ in range(0, M - N + 1):
        B.append(0)
    D = []
    for _ in range(0, M - N + 1):
        C = []
        for j in range(0, M):
            C.append(A[j] * B[j])
        D.append(sum(C))
        B.pop()
        B.insert(0, 0)

    ans = max(D)
    print(f'#{i} {ans}')
