import sys
sys.stdin = open('sample_input(1).txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [[0]*N for _ in range(N)]

    matrix[N//2-1][N//2-1] = 2
    matrix[N//2][N//2] = 2
    matrix[N//2][N//2-1] = 1
    matrix[N//2-1][N//2] = 1

    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1

        matrix[a][b] = c
        for da, db in [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, 1], [1, -1]]:
            step = []

            for j in range(1, N):
                if 0 <= a + da*j < N and 0 <= b + db*j < N:
                    if matrix[a+da*j][b+db*j] == c:
                        for x, y in step[:]:
                            matrix[x][y] = c
                            step.pop(0)
                    elif matrix[a+da*j][b+db*j] == 0:
                        break
                    else:
                        step += [[a + da * j, b + db * j]]
            if step:
                for x, y in step[:]:
                    matrix[x][y] = c
                    step.pop(0)


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