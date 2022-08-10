import sys
sys.stdin = open('input_1209.txt', 'r')

for tc in range(1,11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_list = []
    rd_sum = 0
    ld_sum = 0
    for i in range(100):
        row_sum = 0
        colum_sum = 0
        rd_sum += arr[i][i]
        ld_sum += arr[i][99-i]
        for j in range(100):
            row_sum += arr[i][j]
            colum_sum += arr[j][i]
        sum_list += [row_sum, colum_sum]
    sum_list += [rd_sum, ld_sum]

    max_value = 0
    for i in sum_list:
        if i > max_value:
            max_value = i
    print(f'#{tc} {max_value}')