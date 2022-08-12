chr_a = input()

center_idx = -1
for idx, i in enumerate(chr_a):
    if i == '0':
        center_idx = idx
# print(center_idx)

left_cnt = 0
for i in range(0, center_idx):
    if chr_a[i] == '@':
        left_cnt += 1

right_cnt = 0
for i in range(center_idx, len(chr_a)):
    if chr_a[i] == '@':
        right_cnt += 1

print(left_cnt, right_cnt)