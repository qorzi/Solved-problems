N = int(input())
for i in range(1, N+1):
    M = int(input())
    print(f'#{i}')
    P = ''
    for j in range(1, M+1):
        L = list(input().split())
        for k in range(1,int(L[1])+1):
            P += L[0]
    while len(P) > 10:
        print(P[:10])
        P = P[10:]
    print(P)