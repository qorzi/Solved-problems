import sys
sys.stdin = open('sample_input.txt', 'r')

def f(idx, visited):
    global ans
    global sel
    visited = list(visited)

    if idx == N:
        if len(sel) == N:
            ans += 1
        return

    for i in range(N):
        if visited[idx][i] == 0:
            sel.append(i)
            print(sel)
            for j in range(idx, N):
                visited[j][i] = 1
                if i + (j - idx) < N:
                    visited[j][i+(j-idx)] = 1
                if i - (j - idx) >= 0:
                    visited[j][i-(j-idx)] = 1
            tmp_visit = visited
            print(visited)
            print(id(tmp_visit))
            f(idx+1, tmp_visit)
            sel.pop()
            print(sel)
            visited = tmp_visit
            # for j in range(idx, N):
            #     visited[j][i] = 0
            #     if i + (j - idx) < N:
            #         visited[j][i+(j-idx)] = 0
            #     if i - (j - idx) >= 0:
            #         visited[j][i-(j-idx)] = 0
            print(visited)
            print(id(tmp_visit))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [[0]*N for _ in range(N)]
    sel = []
    ans = 0

    f(0, visited)

    print(f'#{tc} {ans}')
