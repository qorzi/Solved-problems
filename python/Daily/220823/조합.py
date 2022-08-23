#4C2
lst = ['a', 'b', 'c', 'd']
N = 4
M = 2

def f(idx, sidx):
    if sidx == M:
        print(sel)
        return

    if idx == N:

        return

    sel[sidx] = lst[idx]
    f(idx+1, sidx+1)
    f(idx+1, sidx)

sel = [0]*M

f(0, 0)