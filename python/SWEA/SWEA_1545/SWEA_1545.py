N = int(input())

A = ''
for i in range(N+1):
    A += f'{N-i} '
A.strip()
print(A)