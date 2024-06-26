from heapq import heappush, heappop

def prim(N, graph, reverse):
    visited = [False] * (N+1)
    min_heap = [(1, 0)] # (cost, node)
    total_cost = 0

    while min_heap:
        cost, node = heappop(min_heap)

        if visited[node]:
            continue

        visited[node] = True

        if cost == 0: # 오르막길인 경우
            total_cost += 1

        for dc, d in graph[node]:
            if not visited[d]:
                heappush(min_heap, (dc if not reverse else - dc, d))

    return pow(total_cost, 2)

N, M = map(int, input().split()) # 건물의 수, 도로의 수
graph = [[] for _ in range(N+1)]
for _ in range(M+1):
    x, y, cost = map(int, input().split()) # 0은 오르막길, 1은 내리막길
    graph[x].append((cost, y))
    graph[y].append((cost, x))
    
print(prim(N, graph, False)-prim(N, graph, True))
        
