import sys
sys.stdin = open('sample_input.txt')

def select(total_idx, choose_idx, sel):

    if total_idx == N:
        return

    if choose_idx == N//2:
        # print(sel)
        global lst1
        lst1.append(sel[:])
        return

    sel[choose_idx] = total_idx
    # print(sel)
    select(total_idx+1, choose_idx+1, sel)
    select(total_idx+1, choose_idx, sel)

def taste(lst, num):
    taste_value = 0
    for i in range(N//2):
        for j in range(N//2):
            if i > j:
                # print(matrix[lst[num][i]][lst[num][j]], matrix[lst[num][j]][lst[num][i]])
                taste_value += matrix[lst[num][i]][lst[num][j]] + matrix[lst[num][j]][lst[num][i]]
    return taste_value

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    lst1 = []
    select(0, 0, [0]*(N//2))
    # print(lst1)
    lst2 = []
    for j in lst1:
        tmp = []
        for i in range(N):
            if i not in j:
                tmp.append(i)
        lst2.append(tmp)
    # print(lst2)

    ans = 9999
    for i in range(len(lst1)):
        taste_1 = taste(lst1, i)
        taste_2 = taste(lst2, i)
        # print(taste_1, taste_2)
        diff_taste = abs(taste_1-taste_2)
        if diff_taste < ans:
            ans = diff_taste

    print('#{} {}'.format(tc, ans))
    # print()