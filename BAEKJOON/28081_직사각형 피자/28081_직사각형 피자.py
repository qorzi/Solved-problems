w, h, k = map(int, input().split())
n = int(input())
cut_hor = [0]+list(map(int, input().split()))+[w]
m = int(input())
cut_ver = [0]+list(map(int, input().split()))+[h]

pizza = []
for i in range(n+1):
    width = cut_hor[i+1] - cut_hor[i]
    for j in range(m+1):
        height = cut_ver[j+1] - cut_ver[j]
        pizza.append(width*height)

cnt = 0
for piece in pizza:
    if piece <= k:
        cnt += 1

print(cnt)
