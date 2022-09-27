import sys
sys.stdin = open('sample_input.txt', 'r')

def get_password():
    global passwords

    for i in range(4):
        tmp = ''
        for j in range(N//4):
            tmp += lst[i*(N//4)+j]
        passwords += [tmp]

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(str, input()))
    passwords = []

    get_password()
    for _ in range(N):
        tmp2 = lst.pop(0)
        lst.append(tmp2)
        get_password()
    passwords = list(set(passwords))

    passwords_10 = []
    for i in passwords:
        passwords_10 += [int(i, 16)]

    passwords_10.sort(reverse=True)

    print('#{} {}'.format(tc, passwords_10[K-1]))
