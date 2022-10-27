import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    lst = []
    for i in range(N):
        for j in range(N):
            if i > j:
                A = matrix[i][j] + matrix[j][i]
                lst.append(A)
    print(lst)
    ans = 99
    num_lst = len(lst)
    for i in range(num_lst):
        for j in range(i+1, num_lst):
            B = abs(lst[i] - lst[j])
            if B < ans:
                ans = B

    print('#{} {}'.format(tc, ans))