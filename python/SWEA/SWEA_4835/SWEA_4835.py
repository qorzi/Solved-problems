import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tester in range(T):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    # print(num_list)

    #합 리스트
    sum_list = []
    for i in range(N-M+1):
        tmp_value = 0
        for j in range(M):
            tmp_value += num_list[i+j]
        sum_list += [tmp_value]
    # print(sum_list)

    #정렬
    for i in range(len(sum_list)-1, 0, -1):
        for j in range(i):
            if sum_list[j] > sum_list[j+1]:
                sum_list[j], sum_list[j+1] = sum_list[j+1], sum_list[j]


    print(f'#{tester+1} {sum_list.pop()-sum_list[0]}')