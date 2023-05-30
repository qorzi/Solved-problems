N = int(input())
nums = list(map(int, input().split()))
nums.sort()

cumulative_sum = [sum(nums[:i+1]) for i in range(len(nums))]

print(sum(cumulative_sum))
