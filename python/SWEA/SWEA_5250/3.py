import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 최저가 간이 생성
    min_price = 1000*N*N
    dist = [[min_price]*N for _ in range(N)]
    dist[0][0] = 0

    start = [(0,0)]
    while start:
        i, j = start.pop(0)
        # print(dist)
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0 <= i+di < N and 0 <= j+dj < N:
                diff = 0
                if matrix[i+di][j+dj] - matrix[i][j] > 0:
                    diff = matrix[i+di][j+dj] - matrix[i][j]
                if dist[i+di][j+dj] > dist[i][j] + diff + 1:
                    dist[i+di][j+dj] = dist[i][j] + diff + 1
                    start.append((i+di, j+dj))
    ans = dist[N-1][N-1]
    print('#{} {}'.format(tc, ans))