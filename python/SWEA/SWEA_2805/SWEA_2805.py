import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    L = int(input())
    lst = [list(map(int, input())) for _ in range(L)]

    all_sum = 0
    for i in lst:
        all_sum += sum(i)

    subtract_sum = 0
    center_L_index = L//2
    # print(center_L_index)
    for i in range(center_L_index):
        for j in range(center_L_index):
            if i+j < center_L_index:
                subtract_sum += lst[i][j]
                subtract_sum += lst[i][L-1-j]
                subtract_sum += lst[L-1-i][j]
                subtract_sum += lst[L-1-i][L-1-j]
    # print(all_sum, subtract_sum)
    ans = all_sum - subtract_sum

    print(f'#{tc} {ans}')