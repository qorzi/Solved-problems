import sys
sys.stdin = open('sample_input.txt','r')

def go(i, j, current_price):
    global min_price

    if current_price > min_price:
        return

    if i == N-1 and j == N-1:
        if min_price > current_price:
            min_price = current_price
        return

    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0 <= i + di < N and 0 <= j + dj < N:
            if visited[i+di][j+dj] == 0:
                visited[i][j] = 1
                if matrix[i+di][j+dj] - matrix[i][j] > 0:
                    current_price += matrix[i+di][j+dj] - matrix[i][j]
                go(i+di, j+dj, current_price)
                visited[i][j] = 0
                if matrix[i+di][j+dj] - matrix[i][j] > 0:
                    current_price -= matrix[i+di][j+dj] - matrix[i][j]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*(N+1) for _ in range(N+1)]

    # 최저가 간이 생성
    min_price = 0
    for i in range(1, N):
        min_price += matrix[i][0] + matrix[N-1][i]

    # 0,0 -> N-1, N-1 까지 언덕 비용 구하기
    go(0, 0, 0)
    # 거리 비용 더하기
    min_price += (N-1)*2
    print('#{} {}'.format(tc, min_price))
