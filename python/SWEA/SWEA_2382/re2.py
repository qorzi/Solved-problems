import sys
sys.stdin = open('sample_input.txt', 'r')

# 상 1 하 2 좌 3 우 4 제거 0
direction = {1: [-1,0], 2: [1,0], 3: [0,-1], 4: [0,1]}
change_dir = {1:2, 2:1, 3:4, 4:3}
ij_lst = []

T = int(input())
for tc in range(1, T+1):
    N, time, K = map(int, input().split())
    microbe_lst = [list(map(int, input().split())) for _ in range(K)]
    exist = [[0]*N for _ in range(N)]
    warn_bounder = [[0] * N for _ in range(N)]

    # 약품 경계구역
    for i in range(N):
        warn_bounder[0][i] = -1
        warn_bounder[N - 1][i] = -1
        warn_bounder[i][0] = -1
        warn_bounder[i][N - 1] = -1

    # 이차원 배열에 개체수와 방향을 담고 해당 좌표를 다른 리스트로 담는다.
    for microbe in microbe_lst:
        i, j, cnt, go = microbe
        exist[i][j] = [cnt, go]
        ij_lst += [[i, j]]
    print(ij_lst)

    for _ in range(time):
        tmp_ij = []
        while ij_lst:
            i, j = ij_lst.pop(0)
            cnt, dir_num = exist[i][j]
            di, dj = direction[dir_num]

            # 경계로 들어가면, 수는 절반, 방향은 반대가 된다.
            if warn_bounder[i+di][j+dj] == -1:
                cnt = cnt // 2
                dir_num = change_dir[dir_num]

            if exist[i+di][j+dj]:
                ex_cnt, ex_dir_num = exist[i+di][j+dj]
                if cnt > ex_cnt:
                    cnt += ex_cnt
                    exist[i + di][j + dj] = [cnt, dir_num]
                    tmp_ij += [i+di, j+dj]
                    # 중복 좌표 제거
                    re_dx = ij_lst.index([i + di, j + dj])
                    try:
                        ij_lst.remove(re_dx)
                    except:
                        tmp_ij.remove(re_dx)
                elif cnt < ex_cnt:
                    cnt += ex_cnt
                    exist[i + di][j + dj] = [cnt, ex_dir_num]
            else:
                exist[i + di][j + dj] = [cnt, dir_num]
                tmp_ij += [i + di, j + dj]
        ij_lst = tmp_ij

