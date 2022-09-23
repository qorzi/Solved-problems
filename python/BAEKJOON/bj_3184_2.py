def count(i, j):
    O_count = 0
    V_count = 0
    stack = [[i, j]]
    while stack:
        start_i, start_j = stack.pop()
        if visited[start_i][start_j]:
            continue
        visited[start_i][start_j] = 1

        if matrix[start_i][start_j] == 'o':
            O_count += 1
        elif matrix[start_i][start_j] == 'v':
            V_count += 1

        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0 <= start_i + di < R and 0 <= start_j + dj < C:
                if visited[start_i + di][start_j + dj] == 0 and matrix[start_i + di][start_j + dj] != '#':
                    stack += [[start_i + di, start_j + dj]]
    # for i in visited:
    #     print(i)
    return O_count, V_count


R, C = map(int, input().split())
matrix = [list(map(str, input())) for _ in range(R)]
visited = [[0]*C for _ in range(R)]

# 울타리 O 양 V 늑대
stack = []
ans_O = 0
ans_V = 0

for i in range(R):
    for j in range(C):
        if matrix[i][j] != '#' and visited[i][j] == 0:
            O_count, V_count = count(i, j)

            if O_count > V_count:
                V_count = 0
            else:
                O_count = 0
            ans_O += O_count
            ans_V += V_count

print(ans_O, ans_V)