import sys
sys.stdin = open('sample_input.txt')

def choice(N, depth, check_list, current):
    global ans
    depth += 1

    if depth > 4:
        # 현재 조합으로 음식 만들기
        print(current)
        A = matrix[current[0]][current[1]]+matrix[current[1]][current[0]]
        B = matrix[current[2]][current[3]]+matrix[current[3]][current[2]]
        value = abs(A-B)
        if value < ans:

            ans = value

        return

    for i in range(N):
        if check_list[i] == 0:
            check_list[i] = 1
            current.append(i)
            choice(N, depth, check_list, current)
            check_list[i] = 0
            current.pop()

T = int(input())
for tc in range(1, 3+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(i+1, N):
    check_list = [0] * N
    ans = 99
    choice(N, 0, check_list, [])

    print('#{} {}'.format(tc, ans))