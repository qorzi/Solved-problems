R, C, N = map(int, input().split())
grid = [list(input()) for _ in range(R)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

stack = []
for i in range(1, N+1):
    if i == 1:
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 'O':
                    stack.append([i, j])
    elif i % 2:
        while stack:
            i, j = stack.pop()
            grid[i][j] = '.'
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < R and 0 <= ny < C:
                    grid[nx][ny] = '.'

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 'O':
                    stack.append([i, j])
    else:
        grid = [['O']*C for _ in range(R)]
for a in grid:
    print(''.join(a))
