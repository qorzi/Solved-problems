import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = -1
    for i in range(N+1):
        if i**3 == N:
            ans = i
            break
        elif i**3 > N:
            break

    print(f'#{tc} {ans}')