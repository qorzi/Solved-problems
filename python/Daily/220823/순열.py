#4P2
lst = ['a', 'b', 'c', 'd']
N = 4
M = 2

def f(idx):
    if idx == M:
        print(sel)
        return

    for i in range(N):
        if i not in visited:
            visited.append(i)
            sel.append(lst[i])
            f(idx+1)
            visited.pop()
            sel.pop()

visited = []
sel = []

f(0)