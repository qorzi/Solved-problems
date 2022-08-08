import sys
sys.stdin = open('input.txt')

#Gravity

#가로 N 세로 M인 상자가 있고, 내부에 작은 상자가 쌓여있을 때,
#90도 회전 후 낙차가 가장 큰 값은 무엇인가.

#풀이
#박스를 90도로 회전 후, 중력 적용 전과 후를 두 케이스로 나누고
#각각의 낙차값 중 최대값을 추출한다.
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    init_position_list = list(map(int, input().split()))

    #90도 회전하고 중력이 적용 되지 않은 박스 가로 M 세로 N
    Box_gravity_off = []
    for i in init_position_list:
        tmp_list = []
        for j in range(i):
            tmp_list.append(1)
        for k in range(M-i):
            tmp_list.append(0)
        Box_gravity_off += [tmp_list]
    # print(Box_gravity_off)

    #90도 회전하고 중력이 적용된 박스에서 각 column 쌓인 박스 수
    Box_gravity_on = []
    for i in range(M):
        tmp_column_count = 0
        for j in range(N):
            tmp_column_count += Box_gravity_off[j][i]
        Box_gravity_on += [tmp_column_count]
    # print(Box_gravity_on)

    #낙차 모음 리스트
    fall_count_list = []
    for idx_i, i in enumerate(Box_gravity_off):
        for idx_j, j in enumerate(i):
            if j == 1:
                if N - idx_i - Box_gravity_on[idx_j] > 0:
                    fall_count_list += [N - idx_i - Box_gravity_on[idx_j]]
    # print(fall_count_list)

    #낙차 값 중 최대값
    fall_max = 0
    for i in fall_count_list:
        if i >= fall_max:
            fall_max = i
    print(fall_max)



