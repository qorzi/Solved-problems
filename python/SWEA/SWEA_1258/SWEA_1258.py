import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    visited_matrix = [[0]*N for _ in range(N)]
    rc_lst = []

    while True:
        flag = 0
        start = []
        for i in range(N):
            for j in range(N):
                if matrix[i][j] and visited_matrix[i][j] == 0:
                    start += [[i, j]]
                    break
            if start:
                break
        else:
            flag = 1

        while start:
            i, j = start.pop()
            visited_matrix[i][j] = 1

            i_add = 0
            j_add = 0
            if 0 <= j+j_add+1 < N and matrix[i][j++1]:
                while 0 <= j+j_add+1 < N and matrix[i][j+j_add+1]:
                    j_add += 1
            if 0 <= i+i_add+1 < N and matrix[i+1][j]:
                while 0 <= i+i_add+1 < N and matrix[i+i_add+1][j]:
                    i_add += 1
            rc_lst += [[i_add+1, j_add+1]]

            for a in range(i_add+1):
                for b in range(j_add+1):
                    visited_matrix[i+a][j+b] = 1

        if flag:
            break

    # print(rc_lst)
    # 행 크기순으로 정렬
    rc_lst.sort(key=lambda x:x[0])
    # 너비 순으로 정렬
    rc_lst.sort(key=lambda x:x[0]*x[1])
    # print(rc_lst)
    # 출력하기 편하게 1차원 리스트로 담기
    ans_lst = []
    for i in range(len(rc_lst)):
        ans_lst.append(rc_lst[i][0])
        ans_lst.append(rc_lst[i][1])
    print(f'#{tc} {len(rc_lst)}', *ans_lst)



