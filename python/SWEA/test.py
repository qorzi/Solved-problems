arr = ['A', 'B', 'C']  # 재료 리스트
sel = [0, 0, 0]  # 인형뽑기 selection
check = [0, 0, 0]  # 뽑을지 말지 결정하는 리스트


def perm(depth):
    if depth == 3:
        print(sel)
        return

    for i in range(3):
        if not check[i] == 1:
            check[i] = 1
            sel[depth] = arr[i]
            perm(depth+1)
            check[i] = 0

perm(0)