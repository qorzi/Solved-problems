import sys
sys.stdin = open("input.txt", "r")

A = int(input())
B = list(map(int, input().split()))

B.sort()

ans = B[int((A-1)/2)]
print(ans)