s = str(input())

def solution(s):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    str_en = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for idx, i in enumerate(str_en):
        s = s.replace(i, num[idx])
    return int(s)

print(solution(s), end='')