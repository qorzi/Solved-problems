import sys
sys.stdin = open('input (1).txt', 'r')


def inorder(n):
    global ans_char
    if n:
        inorder(l_lst[n])
        ans_char += value_lst[n]
        inorder(r_lst[n])

T = 10
for tc in range(1, T + 1):
    ans_char = ''
    V = int(input())
    E = V - 1
    value_lst = [0] * (V+1)
    l_lst = [0] * (V+1)
    r_lst = [0] * (V+1)
    # print(value_lst)

    for i in range(1, V+1):
        tmp_lst = list(map(str, input().split()))
        # print(tmp_lst)
        value_lst[i] = tmp_lst[1]
        try:
            l_lst[i] = int(tmp_lst[2])
            r_lst[i] = int(tmp_lst[3])
        except:
            pass

    inorder(1)
    print('#{} {}'.format(tc, ans_char))