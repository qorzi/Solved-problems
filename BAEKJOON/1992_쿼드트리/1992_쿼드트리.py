N = int(input())
matrix = [list(input()) for _ in range(N)]


def quard_tree(start_row, start_col, size):
    if size == 1:
        print(matrix[start_row][start_col], end="")
        return
    num = matrix[start_row][start_col]

    for row in range(start_row, start_row + size):
        for col in range(start_col, start_col + size):
            if num != matrix[row][col]:
                print("(", end="")
                size //= 2
                quard_tree(start_row, start_col, size)
                quard_tree(start_row, start_col + size, size)
                quard_tree(start_row + size, start_col, size)
                quard_tree(start_row + size, start_col + size, size)
                print(")", end="")
                return

    print(matrix[start_row][start_col], end="")
    return


quard_tree(0, 0, N)
