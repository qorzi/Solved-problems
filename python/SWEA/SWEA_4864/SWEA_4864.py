import sys
sys.stdin = (open('input_4864.txt', 'r'))

T = int(input())
for tc in range(1, T+1):
    str_1 = input()
    str_2 = input()

    same_str = 0
    str_1_cnt = len(str_1)
    start_idx = []
    for idx, i in enumerate(str_2):
        if i == str_1[0]:
            start_idx += [idx]
    #슬라이싱
    slicing_list = []
    for j in start_idx:
        slicing_list += [str_2[j:j+len(str_1)]]

    #검증
    for k in slicing_list:
        if k == str_1:
            same_str = 1

    print(f'#{tc} {same_str}')
