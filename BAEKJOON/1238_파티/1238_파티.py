from heapq import heappop, heappush

def dijkstra(start, N, graph):
    min_heap = [(0, start)] # (cost, start)

    max_inf = 1e9
    distances = [max_inf] * (N+1)
    distances[0], distances[X] = 0, 0

    while min_heap:
        c_cost, c_node = heappop(min_heap)
        
        if c_cost > distances[c_node]:
            continue

        for n_cost, n_node in graph[c_node]:
            sum_value = n_cost + c_cost
            if sum_value < distances[n_node]:
                distances[n_node] = sum_value
                heappush(min_heap, (sum_value, n_node))

    return distances

N, M, X = map(int, input().split()) # 마을 수, 단방향 도로 개수, 파티 마을
graph_n = [[] for _ in range(N+1)]
graph_r = [[] for _ in range(N+1)]
for _ in range(M):
    x, y, cost = map(int, input().split())
    graph_n[x].append((cost, y))
    graph_r[y].append((cost, x))

n_dist = dijkstra(X, N, graph_n)
r_dist = dijkstra(X, N, graph_r)

max_sum = 0
for i in range(1, N+1):
    tmp = n_dist[i] + r_dist[i]
    max_sum = max(max_sum, tmp)

print(max_sum)