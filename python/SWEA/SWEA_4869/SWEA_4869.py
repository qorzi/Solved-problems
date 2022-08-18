import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    #작은 사각형은 1, 큰사각형은 2로 표현한다.
    #가로 공간은 10을 나눈 small_N으로 한다
    small_N = N//10
    memo = [0]*small_N
    memo[0] = 1
    memo[1] = 3

    if small_N > 2:
        for i in range(2, small_N):
            # 홀수
            if (i+1) % 2:
                memo[i] = memo[i - 1] * 2 - 1
            # 짝수
            elif not (i+1) % 2:
                memo[i] = memo[i - 1] * 2 + 1
    else:
        pass
    # print(small_N, memo)
    ans = memo[small_N-1]
    print(f'#{tc} {ans}')




