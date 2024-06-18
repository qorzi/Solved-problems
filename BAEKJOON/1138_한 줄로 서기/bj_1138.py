N = int(input())
lst = list(map(int, input().split()))
lst.reverse()

line = []
for i in range(N):
    line.insert(lst[i], N - i)

print(" ".join(map(str, line)))