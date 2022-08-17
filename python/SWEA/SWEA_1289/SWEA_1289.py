import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    memo = list(map(int, input()))

    #시작이 0인 경우 제거
    for _ in memo:
        if memo.index(0) == 0:
            memo.pop(0)
        else:
            break

    memo_cnt = len(memo)
    bin_list = [0] * memo_cnt
    cnt = 0
    #시작은 무조건 1이다.
    same_true = 0       #연속된 1을 카운트 하지 않기 위한 판별기
    for idx, i in enumerate(memo):
        if i == 0 and same_true == 1:
            for j in range(memo_cnt-1, idx, -1):
                bin_list[j] = 0
            cnt += 1
            same_true = 0
        elif i == 1 and same_true == 0:
            for j in range(memo_cnt-1, idx, -1):
                bin_list[j] = 1
            cnt += 1
            same_true = 1

        if memo == bin_list:
            break

    print(f'#{tc} {cnt}')
