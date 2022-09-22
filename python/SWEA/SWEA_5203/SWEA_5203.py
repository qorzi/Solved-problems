import sys
sys.stdin = open('sample_input.txt', 'r')

def bady(cards):

    def run_cnt(start, cnt):
        nonlocal max_cnt
        cnt += 1
        if cnt >= 3:
            max_cnt = cnt
            return
        if cards.count(start + 1):
            run_cnt(start + 1, cnt)

    cards.sort()

    for card in cards:
        if cards.count(card) >= 3:
            return 1
        max_cnt = 0
        run_cnt(card, 0)
        if max_cnt >= 3:
            return 1

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    A = []
    B = []
    Awin = 0
    Bwin = 0

    for cdx, card in enumerate(cards):
        max_cnt = 0
        if cdx % 2 == 0:
            A += [card]
            if cdx >= 4:
                Awin = bady(A)
        else:
            B += [card]
            if cdx >= 5:
                Bwin = bady(B)

        if Awin:
            ans = 1
            break
        elif Bwin:
            ans = 2
            break
    else:
        ans = 0

    print('#{} {}'.format(tc, ans))