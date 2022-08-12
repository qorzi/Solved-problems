import sys
sys.stdin = open('input_4861.txt', 'r')

# 회문검사
def search(N, M, arr):
    palindrome = 'None'
    for i in arr:
        for j in range(N-M+1):
            #!주의 for문으로 문자열을 가져올때 인식이 안됨.
            #임시 변수로 문자로 담아서 계산
            tmp_i = str(i)
            slicing_str = tmp_i[j:j+M]
            # print(slicing_str)
            tmp_reverse_str = slicing_str[::-1]
            if slicing_str == tmp_reverse_str:
                palindrome = slicing_str
    return palindrome

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    #90회전
    rot_arr = []
    for i in range(N):
        tmp_str = ''
        for j in range(N):
            tmp_str += arr[j][i]
        rot_arr.append(tmp_str)

    # print(arr)
    # print(rot_arr)

    ans = search(N, M, arr)
    if ans == 'None':
        ans = search(N, M, rot_arr)

    print(f'#{tc} {ans}')
