nums = [0, 1, 0, 3, 2]

left = 0
for (right,num) in enumerate(nums):
    if num != 0 and right != left:
        if nums[left] == 0:
            nums[left] = num
            nums[right] = 0
            left += 1
        right += 1

print(nums)
