import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())
    C = A.replace(B, ',')

    print(f'#{tc} {len(C)}')