def find(x, parents): # 부모 찾기
    if x != parents[x]:
        parents[x] = find(parents[x], parents)  # 경로 압축
    return parents[x]

def union(x, y, parents, rank): # 합치기
    rootX = find(x, parents)
    rootY = find(y, parents)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parents[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parents[rootX] = rootY
        else:
            parents[rootY] = rootX
            rank[rootX] += 1

def kruskal(N, edges):
    parents = list(range(N + 1))
    rank = [0] * (N + 1)
    
    # 간선을 비용 순으로 정렬
    edges.sort(key=lambda x: x[2])
    
    mst_cost = 0
    mst_edges = []

    for u, v, weight in edges:
        if find(u, parents) != find(v, parents):
            union(u, v, parents, rank)
            mst_cost += weight
            mst_edges.append((u, v, weight))

    return mst_cost, mst_edges

# 입력 처리
N = int(input())  # 컴퓨터 수
M = int(input())  # 연결 가능한 선 수
edges = []

for _ in range(M):
    x, y, cost = map(int, input().split())
    edges.append((x, y, cost))

mst_cost, mst_edges = kruskal(N, edges)

# 모든 노드를 연결할 수 있는 경우에만 비용 출력
if len(mst_edges) == N - 1:
    print(mst_cost)
else:
    print("모든 노드를 연결할 수 없습니다.")
