import sys
sys.stdin = open('input_2005.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # print(tc)
    pascal = [[1], [1, 1]]
    index_N = N - 1

    if index_N > 1:
        for j in range(1, index_N):
            tmp = [1]
            for i in range(1, 1+j):
                try:
                    tmp += [pascal[j][i-1]+pascal[j][i]]
                except:
                    pass
            tmp += [1]
            pascal += [tmp]

    print(f'#{tc}')
    for i in range(N):
        print(*pascal[i])