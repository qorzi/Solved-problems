import sys
sys.stdin = open('input_string2.txt', 'r')

for tc in range(1, 7):
    num_int = int(input())

    def itoa(num_int):
        num_str = str(num_int)
        return num_str

    print(f'#{tc} {itoa(num_int)} {itoa(num_int).__class__}')