import sys
sys.stdin = open('input.txt', 'r')

# 1 벽, 0 길, 2 출발점, 3 도착점
T = 10
for tc in range(1, T+1):
    tc_delete = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    visited = [[0]*100 for _ in range(100)]

    # 출발점, 도착점 찾기
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                start = [[i, j]]
            elif maze[i][j] == 3:
                end_i, end_j = i, j

    while start:
        start_i, start_j = start.pop()

        # 왔던 곳이면 넘어가기
        if visited[start_i][start_j]:
            continue

        visited[start_i][start_j] = 1

        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0 <= start_i+di < 100 and 0 <= start_j+dj < 100:
                if visited[start_i+di][start_j+dj] == 0:
                    if maze[start_i+di][start_j+dj] == 0 or maze[start_i+di][start_j+dj] == 3:
                        start.append([start_i+di, start_j+dj])

    if visited[end_i][end_j]:
        ans = 1
    else:
        ans = 0

    print('#{} {}'.format(tc, ans))
