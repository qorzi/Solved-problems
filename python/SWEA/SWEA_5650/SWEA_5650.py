import sys
sys.stdin = open('sample_input.txt', 'r')

value1 = {(-1,0):(1,0), (0,1):(0,-1), (1,0):(0,1), (0,-1):(-1,0)}
value2 = {(1,0):(-1,0), (0,1):(0,-1), (-1,0):(0,1), (0,-1):(1,0)}
value3 = {(1,0):(-1,0), (-1,0):(0,-1), (0,1):(1,0), (0,-1):(0,1)}
value4 = {(1,0):(0,-1), (-1,0):(1,0), (0,1):(-1,0), (0,-1):(0,1)}
value5 = {(1,0):(-1,0), (-1,0):(1,0), (0,1):(0,-1), (0,-1):(0,1)}

def pinball(i, j):
    def wormhole(n, a, b):
        for i in range(N):
            for j in range(N):
                if matrix[i][j] == n and (i != a and j != b):
                    return i, j

    current_i , current_j = i, j
    cnt_lst = []
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        cnt = 0
        current_di, current_dj = di, dj
        while True: # 블랙홀을 만나거나, i,j로 돌아 올때까지
            if 0 <= current_i+di < N and 0 <= current_j+dj < N:
                current_i += di
                current_j += dj
                value = matrix[current_i+current_di][current_j+current_dj]
                print(current_i, current_j, value)
                if value:
                    print('hi')
                    if 6 <= value <= 10: # 웜홀을 만났을 때
                        current_i, current_j = wormhole(value, current_i, current_j)
                    elif value == 1:
                        current_di, current_dj = value1[(current_di, current_dj)]
                        cnt += 1
                    elif value == 2:
                        current_di, current_dj = value1[current_di, current_dj]
                        cnt += 1
                    elif value == 3:
                        current_di, current_dj = value1[current_di, current_dj]
                        cnt += 1
                    elif value == 4:
                        current_di, current_dj = value1[current_di, current_dj]
                        cnt += 1
                    elif value == 5:
                        current_di, current_dj = value1[current_di, current_dj]
                        cnt += 1
            else:
                di = -di
                dj = -dj
                cnt += 1

            if matrix[current_i][current_j] == -1:
                break
            elif current_i == i and current_j == j:
                break
        cnt_lst.append(cnt)
    return max(cnt_lst)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                tmp = pinball(i, j)
                if tmp > ans:
                    ans = tmp

    print('#{} {}'.format(tc, ans))