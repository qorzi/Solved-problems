import sys
sys.stdin = open('sample_input.txt', 'r')

# 높이 조건 확인
def site(matrix, visited):
    cnt_lst = [0]*N
    for i in range(N):
        # 높이가 동일할 때
        for j in range(1, N):
            if matrix[i][0] != matrix[i][j]:
                break
        else:
            cnt_lst[i] = 1
            continue
        # 높이가 다를 때
        flag = False
        for j in range(N-1):
            if matrix[i][j] != matrix[i][j+1]:
                if abs(matrix[i][j] - matrix[i][j+1]) == 1:
                    # i, j 부터 왼쪽
                    if matrix[i][j] - matrix[i][j+1] < 0:
                        if j+1 >= X:
                            for x in range(1, X):
                                if matrix[i][j] != matrix[i][j-x] or visited[i][j] or visited[i][j-x]:
                                    cnt_lst[i] = 0
                                    flag = True
                                    break
                            else:
                                for x in range(X):
                                    visited[i][j-x] = 1
                                cnt_lst[i] = 1
                                # print(i,j,'왼쪽')
                            if flag:
                                break
                        else:
                            cnt_lst[i] = 0
                            break

                    # i, j+1 부터 오른쪽
                    else:
                        if N-(j+1) >= X:
                            for x in range(1, X):
                                if matrix[i][j+1] != matrix[i][j+1+x] or visited[i][j+1] or visited[i][j+1+x]:
                                    cnt_lst[i] = 0
                                    flag = True
                                    break
                            else:
                                for x in range(X):
                                    visited[i][j+1+x] = 1
                                cnt_lst[i] = 1
                                # print(i, j+1, '오른쪽')
                            if flag:
                                break
                        else:
                            cnt_lst[i] = 0
                            break
                else:
                    cnt_lst[i] = 0
                    break

    # print(cnt_lst)

    return sum(cnt_lst)



T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    normal_matrix = [list(map(int, input().split())) for _ in range(N)]
    rotate_matrix = list(zip(*normal_matrix[::-1]))
    normal_visited = [[0]*N for _ in range(N)]
    rotate_visited = [[0] * N for _ in range(N)]
    ans = site(normal_matrix, normal_visited) + site(rotate_matrix, rotate_visited)

    print('#{} {}'.format(tc, ans))
