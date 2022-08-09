import sys
sys.stdin = open('input.txt')

#풀이
#최고점과 최저점을 찾고 그 차이가 1이하가 될 때까지
#최고점에서 최저점으로 상자를 N회 옮긴다.

for T in range(1,11):
    dump_cnt = int(input())
    box_list = list(map(int, input().split()))

    while True:
        #정렬
        for i in range(len(box_list)-1, 0, -1):
            for j in range(i):
                if box_list[j] > box_list[j+1]:
                    box_list[j], box_list[j+1] = box_list[j+1], box_list[j]
        # print(box_list)

        #정렬후, 최대 최소 차이가 1보다 작거나 같으면 Break
        if box_list[len(box_list)-1] - box_list[0] <= 1:
            break
        elif dump_cnt == 0:
            break

        #덤핑
        if box_list[len(box_list)-1] - box_list[0] >= 1:
            dump_cnt -= 1
            box_list[len(box_list)-1] -= 1
            box_list[0] += 1


    print(f'#{T} {box_list[len(box_list)-1] - box_list[0]}')