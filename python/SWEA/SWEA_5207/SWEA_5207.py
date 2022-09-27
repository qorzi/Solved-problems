import sys
sys.stdin = open('sample_input.txt', 'r')

def ejin(lst, num, check):
    global cnt

    l = 0
    r = len(lst)-1
    m = (l+r)//2

    if lst[m] == num:
        cnt += 1
        return

    l_lst = lst[l:m]
    r_lst = lst[m+1:r+1]
    if lst[m] > num and (check == 2 or check == 0):
        check = 1
        ejin(l_lst, num, check)
    elif lst[m] < num and (check == 1 or check == 0):
        check = 2
        ejin(r_lst, num, check)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0

    for i in B:
        if i not in A:
            continue
        ejin(A, i, 0)

    print('#{} {}'.format(tc, cnt))
