heights = [2, 7, 8, 3, 7, 6]

left = 0
right = len(heights) - 1 
maximum_water = 0
while(left < right):
    water_contained = min(heights[left], heights[right]) * (right - left)
    print(heights[left], heights[right], left, right, water_contained)
    maximum_water = max(water_contained, maximum_water)
    if (heights[left] < heights[right]):
        left += 1
    elif(heights[left] > heights[right]):
        right -= 1
    else:
        left += 1
        right -= 1

print(maximum_water)