import sys
sys.stdin = open('sample_input.txt', 'r')

value1 = {(-1,0):(1,0), (0,1):(0,-1), (1,0):(0,1), (0,-1):(-1,0)}
value2 = {(1,0):(-1,0), (0,1):(0,-1), (-1,0):(0,1), (0,-1):(1,0)}
value3 = {(1,0):(-1,0), (-1,0):(0,-1), (0,1):(1,0), (0,-1):(0,1)}
value4 = {(1,0):(0,-1), (-1,0):(1,0), (0,1):(-1,0), (0,-1):(0,1)}
value5 = {(1,0):(-1,0), (-1,0):(1,0), (0,1):(0,-1), (0,-1):(0,1)}

def pinball(i, j):
    current_i , current_j = i, j
    cnt_lst = []
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        cnt = 0
        current_di, current_dj = di, dj
        flag = True
        while flag: # 블랙홀을 만나거나, i,j로 돌아 올때까지
            if 0 <= current_i+current_di < N and 0 <= current_j+current_dj < N:
                current_i += current_di
                current_j += current_dj
                # print(current_i, current_j)
                value = matrix[current_i][current_j]

                if value:
                    # print('value', value, cnt)
                    if 6 <= value <= 10: # 웜홀을 만났을 때
                        current_i, current_j = wormhole[current_i, current_j]
                    elif value == 1:
                        current_di, current_dj = value1[(current_di, current_dj)]
                        cnt += 1
                    elif value == 2:
                        current_di, current_dj = value2[current_di, current_dj]
                        cnt += 1
                    elif value == 3:
                        current_di, current_dj = value3[current_di, current_dj]
                        cnt += 1
                    elif value == 4:
                        current_di, current_dj = value4[current_di, current_dj]
                        cnt += 1
                    elif value == 5:
                        current_di, current_dj = value5[current_di, current_dj]
                        cnt += 1
            else: # 벽을 만났을 때
                current_i += current_di
                current_j += current_dj
                current_di = -current_di
                current_dj = -current_dj
                cnt += 1

            if 0 <= current_i < N and 0 <= current_j < N:
                if matrix[current_i][current_j] == -1:
                    # print('end')
                    flag = False
                elif current_i == i and current_j == j:
                    # print('end')
                    flag = False
        cnt_lst.append(cnt)
        # print(cnt_lst)
    return max(cnt_lst)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 웜홀 찾기기
    hole_tmp = [[] for _ in range(11)]
    wormhole = {}
    for i in range(N):
        for j in range(N):
            if 6 <= matrix[i][j] <= 10:
                hole_tmp[matrix[i][j]].append((i,j))
    # print(hole_tmp)
    for idx in range(6, 11):
        if hole_tmp[idx]:
            # print(hole_tmp[idx][0], hole_tmp[idx][1])
            a, b = hole_tmp[idx][0], hole_tmp[idx][1]
            wormhole[a] = b
            wormhole[b] = a
    # print(wormhole)

    ans = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                # print('start', i, j)
                tmp = pinball(i, j)
                if tmp > ans:
                    ans = tmp

    print('#{} {}'.format(tc, ans))