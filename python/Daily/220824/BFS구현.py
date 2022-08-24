from collections import deque
queue = deque()

lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
V = 7
E = 8

matrix = [[0]*(V+1) for _ in range(V+1)]
visited = []
queue.append(1)

for i in range(E):
    start = lst[i*2]
    end = lst[i*2+1]
    matrix[start][end] = 1
    matrix[end][start] = 1

while queue:
    current = queue.popleft()
    if current not in visited:
        visited.append(current)

    for destination in range(V+1):
        if matrix[current][destination] and destination not in visited:
            queue.append(destination)

print('이동경로:', *visited)

