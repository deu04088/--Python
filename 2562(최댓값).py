nums = []
i = 0
while i < 9:
    a = int(input())
    nums.append(a)
    i += 1
print(max(nums))

for i in range(len(nums)):
    if max(nums) == nums[i]:
        print(i+1)
        
# 문제 조건을 잘 볼 것