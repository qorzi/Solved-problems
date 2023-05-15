def min_swaps(word, a, b):
    num_a = word.count(a)
    num_b = word[:num_a].count(b)
    min_b = num_b

    for i in range(len(word)-num_a):
        num_b = word[i:num_a+1].count(b)
        if min_b < num_b:
            min_b = num_b

    return min_b


word = str(input())
print(min(min_swaps(word, 'a', 'b'), min_swaps(word, 'b', 'a')))
