H, M = map(int, input().split())
B = int(input())
A = 0

while B + M >= 60:
    B = B - 60
    A += 1

H = H + A
M = M + B

if H >= 24:
    H -= 24

print(f'{H} {M}')