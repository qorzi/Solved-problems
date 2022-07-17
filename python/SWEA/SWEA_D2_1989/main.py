N = int(input())

for i in range(1, N+1):
    A = input()
    B = A[::-1]
    if A == B:
        ans = 1
    else:
        ans = 0
    print(f'#{i} {ans}')