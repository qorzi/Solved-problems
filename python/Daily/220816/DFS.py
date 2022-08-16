import sys
sys.stdin = open('input_dfs.txt', 'r')
# 7 8  # Vertex = 7개, Edge = 8개인 그래프가 있을 때,
# 1 2  # 다음 8개의 줄에 연결 정보를 제공
# 1 3
# 2 4
# 2 5  # 2번과 5번이 양방향으로 연결되어 있음!
# 4 6
# 5 6
# 6 7
# 3 7

vertex, edge = map(int, input().split())

adj_matrix = [[0]*(vertex+1) for _ in range(vertex+1)]

for _ in range(edge):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1 #양방향일 때만

stack = [1] #시작점 넣어줌
visited = []

while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)

    for i in range(vertex+1): #갈 수 있는 곳 넣기
        if adj_matrix[current][i] and i not in visited:
            stack.append(i)

print('경로 :', *visited)
# 경로 : 1 3 7 6 5 2 4
