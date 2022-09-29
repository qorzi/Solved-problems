import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 최저가 간이 생성
    min_price = 0
    for i in range(1, N):
        if matrix[i][0] - matrix[i-1][0] > 0:
            min_price += matrix[i][0] - matrix[i-1][0] + 1
        if matrix[N-1][i] - matrix[N-1][i-1] > 0:
            min_price += matrix[N-1][i] - matrix[N-1][i-1] + 1
    visited = [[min_price] * (N) for _ in range(N)]

    start = [(0, 0, 0)]
    while start:
        current = start.pop(0)
        i, j, price = current

        # 현재 비용이 저장된 비용보다 크거나 같으면 넘김
        if price >= visited[i][j] or price > min_price:
            continue
        visited[i][j] = price

        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0 <= i+di < N and 0 <= j+dj < N:
                if matrix[i+di][j+dj] - matrix[i][j] > 0:
                    price += matrix[i+di][j+dj] - matrix[i][j]
                start.append((i+di, j+dj, price))

        if i == N-1 and j == N-1:
            if min_price > price:
                min_price = price
            break

    min_price += (N-1)*2
    print('#{} {}'.format(tc, min_price))