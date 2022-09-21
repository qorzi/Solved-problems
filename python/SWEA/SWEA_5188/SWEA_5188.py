import sys
sys.stdin = open('sample_input.txt', 'r')

# 시작은 항상 0,0 끝은 항상 N-1, N-1
# 뱡향은 항상 오른쪽 아니면 아래
# 우로 N-1칸 아래로 N-1칸
def root_value_sum(i, j, cnt):
    global min_cnt
    if i == N or j == N:
        return

    cnt += matrix[i][j]

    if i == N-1 and j == N-1:
        if cnt < min_cnt:
            min_cnt = cnt

    if cnt > min_cnt:
        return

    for di, dj in [[1,0], [0,1]]:
        root_value_sum(i+di, j+dj, cnt)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    min_cnt = 10*(2*N-1)
    root_value_sum(0, 0, 0)
    print('#{} {}'.format(tc, min_cnt))