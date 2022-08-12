str_a = input()

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alpha:
    if i in str_a:
        str_a = str_a.replace(i, '.')
ans = len(str_a)

print(ans, end='')