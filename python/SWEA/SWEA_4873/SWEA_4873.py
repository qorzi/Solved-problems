import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str_list = list(map(str, input()))
    all_deleted = True
    while all_deleted:
        for i in range(len(str_list)):
            change_cnt = 0
            try:
                if str_list[i] == str_list[i+1]:
                    del str_list[i]
                    del str_list[i]
                    change_cnt += 1
                    break
            except:
                pass

        if change_cnt == 0:
            all_deleted = False
            break

    print(f'#{tc} {len(str_list)}')