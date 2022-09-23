def count(i, j):
    global O_count, V_count

    visited[i][j] = 1
    if matrix[i][j] == 'o':
        O_count += 1
    elif matrix[i][j] == 'v':
        V_count += 1

    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0 <= i + di < R and 0 <= j+dj < C:
            if visited[i+di][j+dj] == 0 and matrix[i+di][j+dj] != '#':
                count(i+di, j+dj)

R, C = map(int, input().split())
matrix = [list(map(str, input())) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
# 울타리 O 양 V 늑대

ans_O = 0
ans_V = 0
for i in range(R):
    for j in range(C):
        O_count = 0
        V_count = 0
        if matrix[i][j] != '#' and visited[i][j] == 0:
            count(i, j)
            if O_count > V_count:
                V_count = 0
            else:
                O_count = 0
            ans_O += O_count
            ans_V += V_count

print(ans_O, ans_V)