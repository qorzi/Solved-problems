import sys
sys.stdin = open('sample_input.txt', 'r')

def rotate(lst_num, dir):
    global visited
    direct = {1:-1, -1:1}
    l, r = matrix[lst_num][-2], matrix[lst_num][2]
    visited[lst_num] = 1

    if lst_num > 3 or lst_num < 0:
        return

    if dir == 1:
        tmp = matrix[lst_num].pop()
        matrix[lst_num] = [tmp] + matrix[lst_num]
    else:
        tmp = matrix[lst_num].pop(0)
        matrix[lst_num] = matrix[lst_num] + [tmp]

    if lst_num+1 <= 3 and visited[lst_num+1] == 0:
        if r != matrix[lst_num+1][-2]:
            rotate(lst_num+1, direct[dir])

    if lst_num-1 >= 0 and visited[lst_num-1] == 0:
        if l != matrix[lst_num-1][2]:
            rotate(lst_num-1, direct[dir])

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    matrix = [list(map(int, input().split())) for _ in range(4)]

    for _ in range(K):
        visited = [0] * 4
        a, b = map(int, input().split())
        rotate(a-1, b)

    ans = matrix[0][0] + matrix[1][0]*2 + matrix[2][0]*4 + matrix[3][0]*8

    print('#{} {}'.format(tc, ans))