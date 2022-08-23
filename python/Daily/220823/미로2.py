import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = set()
    answer = 0

    # 시작 포인트 설정
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                initial_r = i
                initial_c = j

    stack = [(initial_r, initial_c)]

    while stack:
        r, c = stack.pop()
        visited.add((r, c))

        if maze[r][c] == 3:
            answer = 1
            break

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if maze[nr][nc] == 1 or (nr, nc) in visited:
                continue

            stack.append((nr, nc))

    print('#{} {}'.format(tc, answer))