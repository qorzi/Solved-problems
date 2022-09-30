import sys
sys.stdin = open('input.txt', 'r')

solve_num = 0
while True:
    solve_num += 1
    N = int(input())
    if N == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 9*N*N
    dist = [[max_cnt]*N for _ in range(N)]
    dist[0][0] = matrix[0][0]
    start = [(0,0)]
    while start:
        i, j = start.pop(0)
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0 <= i+di < N and 0 <= j+dj < N:
                if dist[i+di][j+dj] > dist[i][j] + matrix[i+di][j+dj]:
                    dist[i+di][j+dj] = dist[i][j] + matrix[i+di][j+dj]
                    start.append((i+di, j+dj))

    print('Problem {}: {}'.format(solve_num, dist[N-1][N-1]))