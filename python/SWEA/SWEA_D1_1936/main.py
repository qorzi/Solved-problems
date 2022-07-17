N = list(map(int, input().split()))
A = N[0]
B = N[1]


def result(A, B):
    if A > B:
        if A == 3 and B == 1:
            ans = 'B'
        else:
            ans = 'A'

    elif B > A:
        if B == 3 and A == 1:
            ans = 'A'
        else:
            ans = 'B'
    return ans


print(result(A, B))