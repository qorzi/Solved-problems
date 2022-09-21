import sys
sys.stdin = open('sample_input.txt', 'r')

def goback(start, cnt, root_cnt):
    global min_cnt
    # 최대 경로에 도달 했다면, 리턴
    if root_cnt == N-1:
        cnt += matrix[start][0]
        if cnt < min_cnt:
            min_cnt = cnt
        cnt -= matrix[start][0]
        return

    # 진행중인 카운트가 최소 값보다 크다면, 리턴
    if cnt > min_cnt:
        return

    # 현재 위치에 도달
    visited[start] = 1

    root_cnt += 1
    for i in range(N):
        if not visited[i] and i != start:
            cnt += matrix[start][i]
            goback(i, cnt, root_cnt)
            cnt -= matrix[start][i]
    visited[start] = 0
    root_cnt -= 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    min_cnt = 100*(N+1)
    visited = [0]*N
    goback(0, 0, 0)

    print('#{} {}'.format(tc, min_cnt))