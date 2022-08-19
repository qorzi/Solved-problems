import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    #정수 판별 .is_interger()
    N_a = N
    a_cnt = 0
    while (N_a/2).is_integer():
        N_a = N_a/2
        a_cnt += 1

    N_b = N
    b_cnt = 0
    while (N_b/3).is_integer():
        N_b = N_b / 3
        b_cnt += 1

    N_c = N
    c_cnt = 0
    while(N_c/5).is_integer():
        N_c = N_c / 5
        c_cnt += 1

    N_d = N
    d_cnt = 0
    while (N_d/7).is_integer():
        N_d = N_d / 7
        d_cnt += 1

    N_e = N
    e_cnt = 0
    while (N_e/11).is_integer():
        N_e = N_e / 11
        e_cnt += 1

    print(f'#{tc}', a_cnt, b_cnt, c_cnt, d_cnt, e_cnt)