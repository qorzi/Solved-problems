import sys
sys.stdin = open('sample_input.txt', 'r')

def ejin(lst, num, check, ex_check):
    global cnt, l, r

    while True:
        m = (l+r)//2

        if ex_check == check:
            return

        if lst[m] == num:
            cnt += 1
            return

        if lst[m] > num:
            ex_check = check
            check = 1
            r = m-1

        elif lst[m] < num:
            ex_check = check
            check = 2
            l = m+1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0

    for i in B:
        if i in A:
            l = 0
            r = len(A) - 1
            ejin(A, i, 0, -1)

    print('#{} {}'.format(tc, cnt))