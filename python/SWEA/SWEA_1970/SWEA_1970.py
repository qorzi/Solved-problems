import sys
sys.stdin = open('input.txt', 'r')

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    cnt_lst = []
    for i in money:
        cnt_lst += [N//i]
        N = N%i

    print(f'#{tc}')
    print(*cnt_lst)