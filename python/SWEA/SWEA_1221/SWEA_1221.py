import sys
sys.stdin = open('input_1221.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    tc_n, N = map(str, input().split())
    str_list = list(map(str, input().split()))
    # print(str_list)

    str_num_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    int_list = [0]*10
    for i in str_list:
        for jdx, j in enumerate(str_num_list):
            if i == j:
                int_list[jdx] += 1

    str_list_change = []
    for idx, i in enumerate(int_list):
        for _ in range(i):
            str_list_change += [str_num_list[idx]]

    print(tc_n)
    print(*str_list_change)
