import sys
sys.stdin = open('input.txt', 'r')

#회문검사
def search(arr):
    max_cnt = 0
    for i in arr:
        for j in range(100):
            for k in range(100):
                pal_cnt = 0
                if i[j] == i[99-k]:
                    l = i[j:99-k+1]
                    reverse_l = l[::-1]
                    if l[0:len(l)//2] == reverse_l[0:len(l)//2]:
                        pal_cnt = len(l)

                    if pal_cnt > max_cnt:
                        max_cnt = pal_cnt
    return max_cnt

for _ in range(10):
    tc = int(input())
    list_v = [list(map(str, input())) for _ in range(100)]

    value_v = search(list_v)

    #회전
    list_h = list(zip(*list_v))

    value_h = search(list_h)

    ans = value_v
    if value_h > value_v:
        ans = value_h

    print(f'#{tc} {ans}')

