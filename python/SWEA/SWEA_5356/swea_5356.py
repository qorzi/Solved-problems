import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str_lst = [list(map(str, input())) for _ in range(5)]

    max_len = 0
    for i in str_lst:
        if len(i) > max_len:
            max_len = len(i)
    v_str = ''
    for i in range(max_len):
        for j in range(5):
            try:
                v_str += str_lst[j][i]
            except:
                pass

    print(f'#{tc} {v_str}')