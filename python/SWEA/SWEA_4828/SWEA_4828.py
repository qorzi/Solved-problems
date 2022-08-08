import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for i in range(T):
    N = int(input())
    input_list = list(map(int, input().split()))

    #오른차순 정렬(버블정렬)
    for j in range(N-1, 0, -1):
        for k in range(j):
            if input_list[k] > input_list[k+1]:
                input_list[k], input_list[k+1] = input_list[k+1], input_list[k]

    print(f'#{i+1} {input_list.pop()-input_list[0]}')
