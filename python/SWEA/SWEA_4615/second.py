import sys
sys.stdin = open('sample_input(1).txt', 'r')

# i, j을 기준으로 8방 탐색
# 흑돌 1, 백돌 2
def change_color(i, j, di, dj, color):
    global steps

    if 0 <= i+di < N and 0 <= j+dj < N:
        if matrix[i+di][j+dj] == 0:
            return
        elif matrix[i+di][j+dj] == color:
            while steps:
                y, x = steps.pop()
                matrix[y][x] = color
        else:
            steps += [[i+di, j+dj]]
            change_color(i + di, j + dj, di, dj, color)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [[0]*N for _ in range(N)]

    matrix[N // 2 - 1][N // 2 - 1] = 2
    matrix[N // 2][N // 2] = 2
    matrix[N // 2][N // 2 - 1] = 1
    matrix[N // 2 - 1][N // 2] = 1

    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1

        matrix[a][b] = c
        for da, db in [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, 1], [1, -1]]:
            steps = []
            change_color(a, b, da, db, c)

        # for i in matrix:
        #     print(i)
        # print('---')

    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                black += 1
            elif matrix[i][j] == 2:
                white += 1

    print('#{} {} {}'.format(tc, black, white))