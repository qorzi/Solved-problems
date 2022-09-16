import sys
sys.stdin = open('input.txt', 'r')

def step(i, j):
    global step_cnt
    global max_cnt
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        if 0 <= i+di < N and 0 <= j+dj < N:
            if matrix[i+di][j+dj] == matrix[i][j] + 1:
                step_cnt += 1
                step(i+di, j+dj)
                step_cnt -= 1
    if max_cnt < step_cnt:
        max_cnt = step_cnt + 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    ans_cnt = 0
    ans_lst = []

    for i in range(N):
        for j in range(N):
            step_cnt = 0
            max_cnt = 0
            step(i, j)

            if ans_cnt <= max_cnt:
                ans_cnt = max_cnt
                ans_lst += [[matrix[i][j], max_cnt]]

    ans_lst.sort(key=lambda x: (-x[1], x[0]))
    # print(ans_lst)
    print('#{} {} {}'.format(tc, ans_lst[0][0], ans_lst[0][1]))



