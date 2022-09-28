# input 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

lst = list(map(int, input().split()))
N = max(lst)+1 # 인덱스가 0부터 시작이니까 +1
matrix = [[0]*N for _ in range(N)]
visited = [0]*N

num = len(lst)//2
for i in range(num):
    matrix[lst[i*2]][lst[i*2+1]] = 1
    matrix[lst[i*2]][lst[i*2+1]] = 1

route = [] # 경로 저장용, 사실 이걸 visited로 써도 됨. 단, 경로 저장으로 비지티드로 쓰면 느려서 안쓰게 됨.

start = [1]
while start:
    current = start.pop(0) # 여기가 pop()이나 pop(0)이냐가 풀이에서 중요.
    if visited[current] != 0: # 방문한적이 있으면 건너띄기
        continue
    visited[current] = 1
    route.append(current)

    for destination in range(N):
        if matrix[current][destination] and visited[destination] == 0: #경로가 존재하고 간적이 없다면, 담아
            start += [destination]

print(route)