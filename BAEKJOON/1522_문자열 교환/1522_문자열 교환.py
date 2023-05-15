# def min_swaps(word, a, b):
#     num_a = word.count(a)
#     num_b = word[:num_a].count(b)
#     min_b = num_b

#     for i in range(len(word)-num_a):
#         num_b = word[i:num_a+1].count(b)
#         if min_b < num_b:
#             min_b = num_b

#     return min_b


# word = str(input())
# print(min(min_swaps(word, 'a', 'b'), min_swaps(word, 'b', 'a')))


def min_swaps(word, a, b):
    num_a = word.count(a)
    num_b = word[:num_a].count(b)
    min_b = num_b

    for i in range(len(word)-num_a):
        if word[i] == b:  # 초기 윈도우에서 오른쪽으로 이동하면서 b가 들어오면 증가
            num_b += 1
        if word[i - num_a] == b:  # 현재 윈도우에서 b가 배출되면 b 감소
            num_b -= 1
        min_b = min(min_b, num_b)

    return min_b


word = str(input())
print(min(min_swaps(word, 'a', 'b'), min_swaps(word, 'b', 'a')))
