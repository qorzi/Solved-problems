def find(x, parents): # 부모 찾기
    while x != parents[x]:
        x = parents[x]
    return x

def union(x, y, parents): # 합치기
    x = find(x, parents)
    y = find(y, parents)

    if x != y:
        parents[y] = x

def cycle_game(N, M, turns):
    parents = [i for i in range(N)]

    for i in range(M):
        x, y = turns[i]
        if find(x, parents) == find(y, parents):
            return i+1
        else:
            union(x, y, parents)

    return 0

N, M = map(int, input().split())
turns = [map(int, input().split()) for _ in range(M)]
print(cycle_game(N, M, turns))
