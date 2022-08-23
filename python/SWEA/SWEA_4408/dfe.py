import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    now_lst = []
    goal_lst = []
    for _ in range(N):
        now, goal = map(int, input().split())
        now_lst.append(now)
        goal_lst.append(goal)
    print(now_lst, goal_lst)