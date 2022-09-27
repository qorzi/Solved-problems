import sys
sys.stdin = open('sample_input.txt', 'r')

def nqueen(cnt):
    global check_lst, ans
    check_num = len(check_lst)

    if cnt > N:
        # print(check_lst)
        ans += 1
        return

    for i in range(N):
        putable = True
        for j in range(1, check_num+1):
            idx = check_lst[-j]
            if idx == i or idx+j == i or idx-j == i:
                putable = False
                break
        if putable:
            check_lst.append(i)
            nqueen(cnt+1)
            check_lst.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [[0]*N for _ in range(N)]
    check_lst = []
    ans = 0
    nqueen(1)
    print('#{} {}'.format(tc, ans))