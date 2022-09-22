import sys
sys.stdin = open('sample_input.txt', 'r')

def truck(start, cnt):
    global max_cnt

    for idx, i in enumerate(t_lst):
        s, e = i

        if s >= start:
            cnt += 1
            truck(e, cnt)
            if cnt > max_cnt:
                max_cnt = cnt
            cnt -= 1
            #정렬에 의거해 가장 처음 조건에 걸리는게 베스트 답이 된다. 바로 리턴.
            return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    t_lst = [list(map(int, input().split())) for _ in range(N)]
    t_lst.sort(key=lambda x:(x[1], x[0]))

    max_cnt = 0
    truck(0, 0)
    print('#{} {}'.format(tc, max_cnt))