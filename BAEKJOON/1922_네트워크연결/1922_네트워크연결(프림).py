from heapq import heappush, heappop

N = int(input())  # 컴퓨터 수
M = int(input())  # 연결 가능한 선 수

graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))

# 초기화
visited = [False] * (N + 1)
min_heap = [(0, 1)]  # (cost, node)
total_cost = 0

while min_heap:
    cost, node = heappop(min_heap)
    
    if visited[node]:
        continue
    
    total_cost += cost
    visited[node] = True
    
    for next_node, next_cost in graph[node]:
        if not visited[next_node]:
            heappush(min_heap, (next_cost, next_node))

print(total_cost)
