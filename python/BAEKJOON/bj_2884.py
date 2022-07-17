H, M = map(int, input().split())

if M >= 45:
    M = M - 45
elif M < 45:
    H = H - 1
    M = M + 15
    if H < 0:
        H = 24 + H

print(f'{H} {M}')