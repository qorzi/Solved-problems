import sys
sys.stdin = open('sample_input.txt', 'r')

# 상 1 하 2 좌 3 우 4
direction = {1: [-1,0], 2: [1,0], 3: [0,-1], 4: [0,1]}

T = int(input())
for tc in range(1, T+1):
    N, time, K = map(int, input().split())
    microbe_lst = [list(map(int, input().split())) for _ in range(K)]
    exist = [[0]*N for _ in range(N)]

    for idx, i in enumerate(microbe_lst):
        exist[i[0]][i[1]] = idx+1
    for i in range(N):
        exist[0][i] = -1
        exist[N-1][i] = -1
        exist[i][0] = -1
        exist[i][N-1] = -1

    # for i in exist:
    #     print(i)

    for _ in range(time):
        for idx, i in enumerate(microbe_lst):
            exist[i[0]][i[1]] = 0
            di, dj = direction[i[3]]

            if exist[i[0]+di][i[1]+dj] == -1:
                i[2] = i[2]//2
                if i[3] == 1:
                    i[3] = 2
                elif i[3] == 2:
                    i[3] = 1
                elif i[3] == 3:
                    i[3] = 4
                elif i[3] == 4:
                    i[3] = 3
                i[0] = i[0]+di
                i[1] = i[1]+dj
            elif exist[i[0]+di][i[1]+dj]:
                # print(exist[i[0]+di][i[1]+dj])
                jdx = exist[i[0]+di][i[1]+dj]
                if i[2] > microbe_lst[jdx][2]:
                    i[2] += microbe_lst[jdx][2]
                    microbe_lst[jdx][2] = 0
                elif i[2] < microbe_lst[jdx][2]:
                    microbe_lst[jdx][2] += i[2]
                    i[2] = 0
                i[0] = i[0] + di
                i[1] = i[1] + dj
            else:
                exist[i[0]+di][i[1]+dj] = idx+1
                i[0] = i[0] + di
                i[1] = i[1] + dj


    total_microbe = 0
    for i in microbe_lst:
        total_microbe += i[2]

    print('#{} {}'.format(tc, total_microbe))