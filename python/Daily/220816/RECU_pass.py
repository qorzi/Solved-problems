import sys
sys.stdin = open('input_dfs.txt', 'r')

def dfs(n):
    if n not in visited:
        visited.append(n)

    for destination in range(vertex+1):
        if adj_matrix[n][destination] and destination not in visited:
            dfs(destination)



vertex, edge = map(int, input().split())

adj_matrix = [[0]*(vertex+1) for _ in range(vertex+1)]

for _ in range(edge):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1 #양 방향일 때

visited = []
dfs(1)

print('이동경로 :', *visited)
# 이동경로 : 1 2 4 6 5 7 3