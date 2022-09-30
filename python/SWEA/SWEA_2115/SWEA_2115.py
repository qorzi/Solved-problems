import sys
sys.stdin = open('sample_input.txt', 'r')

def can():
    global lst
    for i in range(N):
        for j in range(N-M+1):
            tmp = [[i,j]]
            for m in range(M):
                tmp += [matrix[i][j+m]]
            lst += [tmp]

#부분집합 중 최대 구하기
def select(tmp):
    lst = tmp[1:]
    cols = [[]]
    for i in lst:
        size = len(cols)
        for j in range(size):
            cols += [[i]+cols[j]]

    max_cols = []
    for col in cols:
        max_col = 0
        if sum(col) <= C:
            if sum(col) > max_col:
                max_cols += [col]

    max_double = 0
    for i in max_cols:
        double = 0
        for j in i:
            double += j*j

        if double > max_double:
            max_double = double
    return max_double

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    lst = []
    can()
    # print(lst)
    ans = 0
    for i in lst:
        for j in lst:
            # print(i, j)
            if i[0][0] == j[0][0]:
                if j[0][1] - i[0][1] < M:
                    continue
            max_1 = select(i)
            max_2 = select(j)
            if max_1+max_2 > ans:
                ans = max_1+max_2
    print('#{} {}'.format(tc, ans))