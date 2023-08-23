from collections import deque


def grow(arr):
    end_of_zeros = 0
    end_of_ones = 0

    # 왼쪽 테두리는 그대로 유지
    for i in range(M-1, -1, -1):
        if arr:
            grid[i][0] += arr.popleft()

    # 위쪽 테두리 업데이트하며 0과 1이 끝나는 지점을 파악
    for j in range(1, M):
        if not arr:
            break
        growth = arr.popleft()
        grid[0][j] += growth
        if growth == 0:
            end_of_zeros = j
        elif growth == 1:
            end_of_ones = j

    # 나머지 부분 업데이트
    for i in range(1, M):
        for j in range(end_of_zeros + 1, end_of_ones + 1):
            grid[i][j] += 1
    for i in range(1, M):
        for j in range(end_of_ones + 1, M):
            grid[i][j] += 2


M, N = map(int, input().split())
grid = [[1 for _ in range(M)] for _ in range(M)]

for _ in range(N):
    zeros, ones, twos = map(int, input().split())
    arr = deque([0] * zeros + [1] * ones + [2] * twos)
    grow(arr)

for row in grid:
    print(' '.join(map(str, row)))
