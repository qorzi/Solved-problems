from collections import deque

def bfs(start, graph, visited, N, L, R):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    union = [start]
    total_population = graph[start[0]][start[1]]
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    total_population += graph[nx][ny]
                    
    for x, y in union:
        graph[x][y] = total_population // len(union)
    
    return len(union) > 1

def mv_population(N, L, R, graph):
    days = 0
    while True:
        visited = [[False] * N for _ in range(N)]
        is_union = False
        
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    visited[i][j] = True
                    if bfs((i, j), graph, visited, N, L, R):
                        is_union = True
        
        if not is_union:
            break
        
        days += 1
    
    return days

# 입력
N, L, R = map(int, input().split()) # 그래프 크기, 인구차 최소 범위, 인구차 최대 범위
graph = [list(map(int, input().split())) for _ in range(N)] # 각 나라 인구

# 출력
print(mv_population(N, L, R, graph))
