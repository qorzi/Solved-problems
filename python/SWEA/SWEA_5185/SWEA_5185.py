import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, num_16 = map(str, input().split())
    num_10 = int(num_16, 16)

    num_2 = bin(num_10)

    ans = num_2[2:]
    N_2 = int(N)*4 - len(ans)
    for i in range(N_2):
        ans = '0'+ans

    print('#{} {}'.format(tc, ans))