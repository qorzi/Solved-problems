def bellman_ford(start):
    distance = [float('inf') for _ in range(n+1)]
    distance[start] = 0
    for i in range(n):  # N번 반복
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if distance[cur] != float('inf') and distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost
                # N번째 반복에서 값이 갱신되면 음수 사이클 존재
                if i == n - 1:
                    return True
    return distance


n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

distances = bellman_ford(1)

if distances == True:
    print(-1)
else:
    for d in distances[2:]:
        if d == float('inf'):
            print(-1)
        else:
            print(d)
