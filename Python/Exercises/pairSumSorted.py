nums =  [0, -1, 2, -3, 1]


# pairs = { num: 7-num for num in nums}
# sum_pairs = [ (num,pair) for (num,pair) in pairs.items() if pairs[num] in nums]
# print(sum_pairs)

def pair_sum_sorted(array,start, target):
    left = start
    right = len(array) - 1
    pairs = []
    while left < right:
        sum = array[left] + array[right]
        if sum == target:
            pairs.append([array[left], array[right]])
            left += 1 # To avoid duplicate '[b, c]' pairs, skip 'b' if it’s the same as the # previous number.
            while left < right and array[left] == array[left - 1]:
                left += 1
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            right -= 1

    return pairs
pairs = []
for index,num in enumerate(sorted(nums)):
    target = -num
    if target < 0:
        break
    print(sorted(nums))
    print(target)
    pairs.append(pair_sum_sorted(array=nums, start=index+1, target=target))

print(pairs)
