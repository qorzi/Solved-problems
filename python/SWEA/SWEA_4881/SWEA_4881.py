import sys
sys.stdin = open('sample_input.txt', 'r')

def f(idx, total):
    global min_sum
    #재귀가 끝날때, 현재의 합이 min_sum보다 작으면 최소값
    if idx == N:
        if total < min_sum:
            min_sum = total
        return

    #현재의 합이 min_sum을 넘어서면 리턴
    if total > min_sum:
        return

    for i in range(N):
        if i not in checked_row:
            checked_row.append(i)   #지금 방문중이니 어펜드
            f(idx+1, total+matrix[idx][i])
            checked_row.pop()   #방문 끝내고 나가니 팝


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    checked_row = []   #행 선택 유무를 담는 상자
    min_sum = 10*N    #최소값을 담을 변수

    f(0, 0) #실행

    print(f'#{tc} {min_sum}')
