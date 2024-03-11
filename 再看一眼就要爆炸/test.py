
nums = [3,2,4]
target = 6
point1 = 0
point2 = 1
while (nums[point1] + nums[point2] != target):
    if point2 == point1:
        point2 += 1
    if point2 == len(nums) - 1:
        print(11, point1, point2)
        point1 += 1
        point2 = point1 + 1
    elif point2 <= len(nums) - 2:
        print(12, point1, point2)
        point2 += 1
        print(22, point1, point2)
        print(nums[point1], nums[point2])
    print(point1, point2)
print(111, point1, point2)
