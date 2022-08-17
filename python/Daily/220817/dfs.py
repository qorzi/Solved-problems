adj_list = [[1, 2], [0, 3, 4], [0, 4], [1, 5], [1, 2, 5], [3, 4, 6], [5]]

#시작점 v, 정점의 갯수 N
def dfs(v, N):
    visited = [0]*N
    stack = [0]*N
    top = -1

    visited[v] = 1      # 시작점 방문
    while True:
        for w in adj_list[v]:
            if visited[w] == 0:     # v의 인접리스트중 방문 안한 w가 있으면
                top += 1        #push(v)
                stack[top] = v
                v = w       # v <- w
                visited[w] = 1
                break       #for break
        else:       # w가 없으면
            if top != -1:       # 스택이 비어있지 않은 경우
                v = stack[top]      # pop 되돌아가기
                top -= 1
            else:
                break       # while break