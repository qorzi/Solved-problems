def subtree(lst):


N = int(input())
in_lst = list(map(int, input().split()))
post_lst = list(map(int, input().split()))

# 포스트의 마지막은 루트 값
# 프리의 시작이 루트 값
# 인의 중간이 루트 값
# -> 각 서브 트리의 루트를 담으면 프리 ( 좌 -> 우 )

ord_lst = []

root_value = post_lst[-1]
ord_lst += [root_value]
m = in_lst.index(root_value)
l_tree = in_lst[:m]
r_tree = in_lst[m+1:]
while l_tree:

    print(l_tree, root_value, r_tree)

