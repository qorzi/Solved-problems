import sys
sys.stdin = open('sample_input.txt', 'r')

# 상 1 하 2 좌 3 우 4 제거 0
direction = {1: [-1,0], 2: [1,0], 3: [0,-1], 4: [0,1]}
change_dir = {1:2, 2:1, 3:4, 4:3}

T = int(input())
for tc in range(1, T+1):
    N, time, K = map(int, input().split())
    microbe_lst = [list(map(int, input().split())) for _ in range(K)]
    exist = [[0]*N for _ in range(N)]

    for idx, i in enumerate(microbe_lst):
        exist[i[0]][i[1]] = idx+1

    for _ in range(time):
        for idx in range(K):
            if microbe_lst[idx]:
                i, j, cnt, go = microbe_lst[idx]
                di, dj = direction[go]
                exist[i][j] = 0
                if i+di == 0 or i+di == N-1 or j+dj == 0 or j+dj == N-1:
                    cnt = cnt//2
                    go = change_dir[go]

                if exist[i+di][j+dj]:
                    jdx = exist[i+di][j+dj]-1
                    j_cnt = microbe_lst[jdx][2]
                    if cnt > j_cnt:
                        cnt += j_cnt
                        microbe_lst[jdx] = []
                        i += di
                        j += dj
                        exist[i][j] = idx + 1
                        microbe_lst[idx] = [i, j, cnt, go]
                    else:
                        microbe_lst[jdx][2] += cnt
                        microbe_lst[idx] = []

                else:
                    i += di
                    j += dj
                    exist[i][j] = idx + 1
                    microbe_lst[idx] = [i, j, cnt, go]


        # for i in microbe_lst:
        #     print(i)
        # print('---')

    total_microbe = 0
    for i in microbe_lst:
        if i:
            total_microbe += i[2]

    print('#{} {}'.format(tc, total_microbe))