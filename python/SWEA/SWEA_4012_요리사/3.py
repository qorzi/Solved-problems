import sys
sys.stdin = open('sample_input.txt')

def select(total_idx, choose_idx, sel):

    if total_idx == N:
        return

    if choose_idx == N//2:
        # print(sel)
        return
    sel[choose_idx] = total_idx
    print(sel)
    select(total_idx+1, choose_idx+1, sel)
    select(total_idx+1, choose_idx, sel)

T = int(input())
for tc in range(1, 3+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    select(0, 0, [0]*(N//2))
    print()