import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    sdoku_lst = [list(map(int, input().split())) for _ in range(9)]
    verification = {1, 2, 3, 4, 5, 6, 7, 8, 9} #같은 값이 존재하는지 확인. 순서 상관없는 set

    ans = 1
    tmp_set_h = set()
    tmp_set_v = set()
    for i in range(9):
        tmp_set_h = set()
        tmp_set_v = set()
        for j in range(9):
            # 가로검증
            tmp_set_h.add(sdoku_lst[i][j])
            if j == 8 and tmp_set_h != verification:        #가로로 리스트를 전부 확인하고,
                ans = 0                                     #verification과 다르다면 멈춤
                break
            # 세로검증
            tmp_set_v.add(sdoku_lst[j][i])
            if j == 8 and tmp_set_v != verification:        #세로로 리스트를 전부 확인하고,
                ans = 0                                     #verification과 다르다면 멈춤
                break

    # 3x3 검증
    # 각 사각형의 좌측 상단 좌료를 위한 더블포문
    for i in range(3):
        tmp_set_3x3 = set()
        for j in range(3):
            # 3x3 인덱싱을 위한 더블포문
            for k in range(3):
                for l in range(3):
                    tmp_set_3x3.add(sdoku_lst[3*i + k][3*j + l])
                    if k == 2 and l == 2 and tmp_set_3x3 != verification:       #3x3을 전부 확인하고
                        ans = 0                                                 #verification과 다르다면 멈춤
                        break

    print(f'#{tc} {ans}')