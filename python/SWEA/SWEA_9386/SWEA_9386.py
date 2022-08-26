import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    M = int(input())
    N = input()

    cnt_lst = []
    cnt = 0
    for i in N:
        if i == '1':
            cnt += 1
        else:
            cnt_lst += [cnt]
            cnt = 0
    else:
        cnt_lst += [cnt]
    print(cnt_lst)

    print(f'#{tc} {max(cnt_lst)}')
