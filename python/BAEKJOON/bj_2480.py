A, B, C = map(int, input().split())
N = 0
if A == B == C:
    N = 10000+A*1000
elif A == B:
    N = 1000+A*100
elif C == B:
    N = 1000+B*100
elif C == A:
    N = 1000+C*100
else:
    if A >= B and A >= C:
        N = A*100
    elif B >= A and B >= C:
        N = B*100
    elif C >= A and C >= B:
        N = C*100

print(N)

