import sys
sys.stdin = open('input_4843.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    sp_arr = []
    cnt = 5
    while cnt > 0:
        cnt -= 1
        max_N = 0
        for i in arr:
            if i > max_N:
                max_N = i
        else:
            sp_arr += [max_N]
            arr.remove(max_N)

        min_N = arr[0]
        for i in arr:
            if i < min_N:
                min_N = i
        else:
            sp_arr += [min_N]
            arr.remove(min_N)

    print(f'#{tc}', *sp_arr)

