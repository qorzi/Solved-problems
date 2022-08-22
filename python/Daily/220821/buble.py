arr = [3, 4, 5, 2, 2, 9, 8, 6]
N = len(arr)
for i in range(N-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)