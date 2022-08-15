N_switch = int(input())
switch_list = list(map(int, input().split()))

switching = {1:0, 0:1}

N = int(input())
for _ in range(N):
    gender, num = map(int, input().split())
    
    #남자
    if gender == 1:
        switch_idx = num -1
        while switch_idx < N_switch:
            switch_list[switch_idx] = switching[switch_list[switch_idx]]
            switch_idx += num

    #여자
    if gender == 2:
        #대칭 확인
        num -= 1
        switch_list[num] = switching[switch_list[num]]
        i = 1
        while num-i >= 0 and num+i < N_switch and switch_list[num-i] == switch_list[num+i]:
            switch_list[num-i] = switching[switch_list[num-i]]
            switch_list[num+i] = switching[switch_list[num+i]]
            i += 1
    
for i in range(0, N_switch, 20):
    print(*switch_list[i:i+20])