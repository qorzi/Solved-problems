import sys
sys.stdin = open('sample_input.txt', 'r')

def search(matrix):
    for i in matrix:
        print(i)
    print('---')

# 상 1 하 2 좌 3 우 4
direction = {1: [-1,0], 2: [1,0], 3: [0,-1], 4: [0,1]}
change_dir = {1:2, 2:1, 3:4, 4:3}

T = int(input())
for tc in range(1, 1+1):
    N, time, K = map(int, input().split())
    microbe_lst = [list(map(int, input().split())) for _ in range(K)]
    matrix = [[[] for _ in range(N)] for _ in range(N)]
    warn_bounder = [[0] * N for _ in range(N)]

    # 약품 경계구역
    for i in range(N):
        warn_bounder[0][i] = -1
        warn_bounder[N - 1][i] = -1
        warn_bounder[i][0] = -1
        warn_bounder[i][N - 1] = -1

    # 배치
    for microbe in microbe_lst:
        mi, mj, m_cnt, m_direct = microbe
        matrix[mi][mj] += [[m_cnt, m_direct]]
    search(matrix)
    # 실행
    for _ in range(time):
        # 탐색 및 이동
        for i in range(0, N):
            for j in range(0, N):
                if matrix[i][j]:
                    micro = matrix[i][j]
                    matrix[i][j] = []
                    cnt, direct = micro.pop()
                    di, dj = direction[direct]

                    # 경계로 들어가면, 수는 절반, 방향은 반대가 된다.
                    if warn_bounder[i + di][j + dj] == -1:
                        cnt = cnt // 2
                        direct = change_dir[direct]

                    matrix[i+di][j+dj].append([cnt, direct])
                    search(matrix)
        print('이동 후')
        search(matrix)
        print('합치기')
        # 합치기
        for i in range(0,N):
            for j in range(0,N):
                tmp_sum = 0
                tmp_cnt = 0
                tmp_dir = 0
                if len(matrix[i][j]) >= 2:
                    for microbe in matrix[i][j]:
                        tmp_sum += microbe[0]
                        if microbe[0] > tmp_cnt:
                            tmp_cnt = microbe[0]
                            tmp_dir = microbe[1]
                    matrix[i][j] = [[tmp_sum, tmp_dir]]
        search(matrix)

    # 전체 수 카운트
    total_microbe = 0
    for i in microbe_lst:
        if i:
            total_microbe += i[2]

    print('#{} {}'.format(tc, total_microbe))