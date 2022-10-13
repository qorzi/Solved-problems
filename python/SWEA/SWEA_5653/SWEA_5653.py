import sys
sys.stdin = open('sample_input.txt', 'r')

# 사방 번식
def breeding(i, j):
    pass
    time = matrix[i][j]
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= i+di < N and 0 <= j+dj < M and cnt_visited[i+di][j+dj] == 0:
            cnt_visited[i+di][j+dj] = time

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # 세로, 가로, 배양시간
    matrix = [list(map(int, input().split())) for _ in range(N)]
    cnt_visited = matrix[:]

    for i in range(N):
        for j in range(M):
