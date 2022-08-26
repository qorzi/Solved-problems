import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(str, input())) for _ in range(N)]
    # print(matrix)
    pass_flag = False
    #좌우 검증
    if not pass_flag:
        for i in range(N):
            for j in range(N-5+1):
                if matrix[i][j] == 'o' and matrix[i][j+1] == 'o' and matrix[i][j+2] == 'o' \
                        and matrix[i][j+3] == 'o' and matrix[i][j+4] == 'o':
                    pass_flag = True
                    break
            if pass_flag:
                break

    #상하 검증
    if not pass_flag:
        for i in range(N):
            for j in range(N-5+1):
                if matrix[j][i] == 'o' and matrix[j+1][i] == 'o' and matrix[j+2][i] == 'o' \
                        and matrix[j+3][i] == 'o' and matrix[j+4][i] == 'o':
                    pass_flag = True
                    break
            if pass_flag:
                break

    #좌측 하단 대각선 검증
    if not pass_flag:
        tmp = [[] for _ in range(2*N-1)]
        for i in range(N):
            for j in range(N):
                tmp[i+j] += [matrix[i][j]]
        for i in tmp:
            if len(i) >= 5:
                cnt = 0
                for j in i:
                    if j == 'o':
                        cnt += 1
                        if cnt == 5:
                            pass_flag = True
                            break
                    else:
                        cnt = 0
            if pass_flag:
                break

    # 우측 하단 대각선 검증
    if not pass_flag:
        matrix_90 = list(map(list, zip(*matrix[::-1])))
        tmp = [[] for _ in range(2 * N - 1)]
        for i in range(N):
            for j in range(N):
                tmp[i + j] += [matrix_90[i][j]]
        for i in tmp:
            if len(i) >= 5:
                cnt = 0
                for j in i:
                    if j == 'o':
                        cnt += 1
                        if cnt == 5:
                            pass_flag = True
                            break
                    else:
                        cnt = 0
            if pass_flag:
                break

    if pass_flag:
        ans = 'YES'
    else:
        ans = 'NO'
    print(f'#{tc} {ans}')