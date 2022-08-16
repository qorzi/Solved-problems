import sys
sys.stdin = open('input_dfs.txt', 'r')

vertex, edge = map(int, input().split())
matrix = [[0]*(vertex+1) for _ in range(vertex+1)]

for _ in range(edge):
    start, end = map(int, input().split())
    matrix[start][end] = 1
    matrix[end][start] = 1

stack = [1]
visited = []

while stack:
    current =stack.pop()
    if current not in visited:
        visited.append(current)

    for destination in range(vertex+1):
        if matrix[current][destination] and destination not in visited:
            stack.append(destination)

print('경로 :', visited)
