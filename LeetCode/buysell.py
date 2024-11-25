nums = [7,6,4,3,1]
count  =[0]
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i] < nums[j]:
            sums = nums[j] - nums[i]
            count.append(sums)
print(count)
print(max(count))