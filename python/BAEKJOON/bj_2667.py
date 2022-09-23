def search():
    for z in visited_mat:
        print(z)
    print('---')

def detect(i, j):
    global cnt

    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0 <= i+di < N and 0 <= j+dj < N:
            if matrix[i+di][j+dj] == 1 and visited_mat[i+di][j+dj] == 0:
                visited_mat[i+di][j+dj] = 1
                cnt += 1
                detect(i+di, j+dj)

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
visited_mat = [[0]*N for _ in range(N)]

cnt_lst = []
for i in range(N):
    for j in range(N):
        cnt = 0
        if matrix[i][j] and visited_mat[i][j] == 0:
            detect(i, j)
            if cnt == 0:
                cnt = 1
            cnt_lst += [cnt]
            search()

cnt_lst.sort()

print(len(cnt_lst))
for i in cnt_lst:
    print(i)

# ----

# N = int(input())
# matrix = [list(map(int, input())) for _ in range(N)]
# visited_mat = [[0]*N for _ in range(N)]
#
# stack = []
# cnt_lst = []
# num = 0
# while True:
#     for i in range(N):
#         flag = 0
#         for j in range(N):
#             if matrix[i][j] and visited_mat[i][j] == 0:
#                 stack.append([i, j])
#                 flag = 1
#                 num += 1
#                 break
#         if flag:
#             break
#
#     cnt = 0
#     if not stack:
#         break
#
#     while stack:
#         start_i, start_j = stack.pop(0)
#         if visited_mat[start_i][start_j] == 0:
#             visited_mat[start_i][start_j] = 1
#             cnt += 1
#
#         for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
#             if 0 <= start_i+di < N and 0 <= start_j+dj < N:
#                 if matrix[start_i+di][start_j+dj] == 1 and visited_mat[start_i+di][start_j+dj] == 0:
#                     stack += [[start_i + di, start_j + dj]]
#
#     cnt_lst += [cnt]
# cnt_lst.sort()
# print(num)
# for i in cnt_lst:
#     print(i)