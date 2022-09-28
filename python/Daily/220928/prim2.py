def prim2(r, V):
    MST = [0]*(V+1) # 비지티드
    MST[r] = 1
    s = 0
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 1: # 현재 MST와 연결된 간선 중에
                for j in range(V+1):
                    if adjM[i][j] > 0 and MST[j] == 0 and minV > adjM[i][j]:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1
    return s

V, E = map(int, input().split())
adjM = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w

print(prim2(0, V)) # MST 가중치의 합이 리턴