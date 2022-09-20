import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    i = 0
    tmp = N
    ans = ''
    while True:
        i -= 1
        if tmp >= 2**i:
            tmp -= 2**i
            ans += '1'
        else:
            ans += '0'

        if tmp == 0:
            break

    if len(ans) > 12:
        ans = 'overflow'
    print('#{} {}'.format(tc, ans))