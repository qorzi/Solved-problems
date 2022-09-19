import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    password_lst = [input() for _ in range(N)]

    code_list = {
            '0001101': 0,
            '0011001': 1,
            '0010011': 2,
            '0111101': 3,
            '0100011': 4,
            '0110001': 5,
            '0101111': 6,
            '0111011': 7,
            '0110111': 8,
            '0001011': 9
        }

    flag = 0
    for word in password_lst:
        # print(word)
        for i in range(M):
            if word[-i] == '1':
                password = word[M-i-55:M-i+1]
                # print(password)
                flag = 1
                break
        if flag:
            break

    odd_num = 0
    even_num = 0
    for i in range(8):
        # print(code_list[password[7*i:7*(i+1)]])
        # 홀
        if i == 0 or i == 2 or i == 4 or i == 6:
            odd_num += int(code_list[password[7*i:7*(i+1)]])
        # 짝
        else:
            even_num += int(code_list[password[7*i:7*(i+1)]])
    # print(even_num, odd_num)

    if (odd_num*3 + even_num) % 10 == 0:
        ans = even_num + odd_num
    else:
        ans = 0

    print('#{} {}'.format(tc, ans))