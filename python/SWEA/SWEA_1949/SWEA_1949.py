import sys
sys.stdin = open('sample_input.txt', 'r')

# 사방 탐색 재귀, 진행 중에 얻게 되는 맥스 카운트를 가지고 간다.
def root_cnt(i, j):
    global cnt
    global max_cnt
    # print('i j cnt', i, j, cnt) if tc == 3 else 0

    for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
        if 0 <= i+di < N and 0 <= j+dj < N:
            if matrix[i][j] > matrix[i+di][j+dj]:
                cnt += 1
                root_cnt(i+di, j+dj)
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt -= 1

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 봉우리 높이 구하기
    tmp_max = 0
    for i in matrix:
        if tmp_max < max(i):
            tmp_max = max(i)

    # 봉우리 좌표 구하기, start_ij에 담아둔다.
    start_ij = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == tmp_max:
                start_ij += [[i, j]]
    # print(start_ij)

    # 공사를 하지 않은 경우,
    max_lst = [] #맥스 카운트를 담을 리스트
    for lst in start_ij:
        i, j = lst
        cnt = 1
        max_cnt = 0
        root_cnt(i, j)
        max_lst += [max_cnt]

    #공사를 한 경우, 공사 깊이는 1부터 K까지
    for minus_value in range(1, K+1):
        for a in range(N):
            for b in range(N):
                # print(a, b, minus_value) if tc == 3 else 0
                matrix[a][b] -= minus_value
                for lst in start_ij:
                    i, j = lst
                    cnt = 1
                    max_cnt = 0
                    root_cnt(i, j)
                    max_lst += [max_cnt]
                matrix[a][b] += minus_value

    print('#{} {}'.format(tc, max(max_lst)))