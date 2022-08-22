arr = [3, 4, 5, 2, 2, 9, 8, 6]
N = len(arr)
sorted_arr = [0]*N
c_arr = [0] * (max(arr) + 1)
print(arr)

#카운팅 - 값을 인덱스로 두고 해당 인덱스에 갯수 저장
for i in arr:
    c_arr[i] += 1
print(c_arr)

#누적 - 정렬된 리스트의 인덱스를 정해주기 위한 수 누적
#가장 작은 수부터 인덱스 0을 부여, 이후 +1 됨
for j in range(1, len(c_arr)):
    c_arr[j] += c_arr[j-1]
print(c_arr)

#카운팅 값을 빼면서 정렬
for k in range(N): # range(N-1, -1, -1) 가능
    c_arr[arr[k]] -= 1 # 인덱스를 0 0부터 채우기 위한 방책
    sorted_arr[c_arr[arr[k]]] = arr[k] # 존재하는 요소의 인덱스만 오른쪽부터 채움
print(sorted_arr)