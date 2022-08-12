import sys
sys.stdin = open('input_string1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str_1 = input()

    print(f'#{tc} {str_1[::-1]}')