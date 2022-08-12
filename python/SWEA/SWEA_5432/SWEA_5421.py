import sys
sys.stdin = open('input_5421.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    pipe = list(map(str, input()))
    num = (len(pipe)+1)//2
    print(pipe)

    lazer_idx = []
    pipe_star_idx = []
    pipe_end_idx = []
    for i in range(len(pipe)):
        if pipe[i] == '(' and pipe[i+1] == ')':
            lazer_idx += [i]
        elif pipe[i] == ')' and pipe[i-1] == '(':
            pass
        elif pipe[i] == '(':
            pipe_star_idx += [i]
    for k in range(len(pipe))
        elif pipe[i] == ')':
            pipe_end_idx += [i]

    print(lazer_idx)

    cut_cnt = 0
    for j in lazer_idx:
        for k in range(len(pipe_star_idx)):
            if pipe_star_idx[k]< j < pipe_end_idx[k]:
                cut_cnt += 1


    print(f'#{tc} {cut_cnt}')
