import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    lst_2 = []
    for i in range(N-1):
        for j in range(i+1, N):
            lst_2 += [lst[i]*lst[j]]
    # print(lst_2)

    lst_3 = []
    for i in lst_2:
        tmp_i = str(i)
        for j in range(len(tmp_i)-1):
            if tmp_i[j+1] >= tmp_i[j]:
                pass
            else:
                break
        else:
            lst_3 += [i]
    # print(lst_3)

    if lst_3:
        max_int = max(lst_3)
    else:
        max_int = -1

    print(f'#{tc} {max_int}')

