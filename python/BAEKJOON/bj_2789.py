a = list(input())
b = 'CAMBRIDGE'

for i in b:
    for jdx, j in enumerate(a):
        if i == j:
            del a[jdx]

for i in list_a:
    print(i, end='')

a = "CAMBRIDGE"
b = list(input())
for i in a:
    for j in range(len(b)):
        if i == b[j]:
            b[j] = ''
for i in b:
    print(i, end='')