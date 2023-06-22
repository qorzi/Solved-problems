w, h, k = map(int, input().split())
n = int(input())
cut_ver = [0] + list(map(int, input().split())) + [h]
m = int(input())
cut_hor = [0] + list(map(int, input().split())) + [w]

diff_hor = sorted([cut_hor[i+1] - cut_hor[i] for i in range(m+1)])
diff_ver = sorted([cut_ver[j+1] - cut_ver[j] for j in range(n+1)])

cnt = 0
i, j = 0, n
while i < m+1 and j >= 0:
    if diff_hor[i] * diff_ver[j] <= k:
        cnt += j + 1
        i += 1
    else:
        j -= 1

print(cnt)
