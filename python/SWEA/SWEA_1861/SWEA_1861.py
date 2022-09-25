import sys
sys.stdin = open('input.txt', 'r')

def go(i, j, cnt):
    global max_cnt

    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0 <= i+di < N and 0 <= j+dj < N:
            if visited[i+di][j+dj] == 0 and matrix[i][j] + 1 == matrix[i+di][j+dj]:
                visited[i][j] = 1
                cnt += 1
                go(i+di, j+dj, cnt)
                visited[i][j] = 0
                cnt -= 1

    if max_cnt < cnt:
        max_cnt = cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    # for i in matrix:
    #     print(i)

    max_lst = []
    for i in range(N):
        for j in range(N):
            max_cnt = 0
            start = matrix[i][j]
            go(i, j, 1)
            max_lst += [[max_cnt, start]]


    max_lst.sort(key=lambda x:(-x[0], x[1]))
    print('#{} {} {}'.format(tc, max_lst[0][1], max_lst[0][0]))