import sys
sys.stdin = open('input_4839.txt', 'r')

def cnt(P, N):
    start = 1
    end = P
    cnt_N = 0
    while True:
        middle = (start + end) // 2
        cnt_N += 1
        if N > middle:
            start = middle
        elif N < middle:
            end = middle
        elif middle == N:
            break
        #찾고자 하는 페이지가 시작이나 엔드 페이지일 경우, 무한루프 파기
        elif N == P or N == start:
            break
    return cnt_N

T = int(input())
# T = 1
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    # P, A, B = 3, 3, 2

    cnt_A=cnt(P, A)
    cnt_B=cnt(P, B)
    # print(cnt_A, cnt_B)
    ans = 0
    if cnt_A == cnt_B:
        ans = 0
    elif cnt_A > cnt_B:
        ans = 'B'
    elif cnt_B > cnt_A:
        ans = 'A'

    print(f'#{tc} {ans}')