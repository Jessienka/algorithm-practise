class List:
    pass

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         point1 = 0
#         point2 = 1
#         while (nums[point1] + nums[point2] != target):
#             if point2 == point1:
#                 point2 += 1
#             if point2 == len(nums) - 1:
#                 point1 += 1
#                 point2 = point1 + 1
#             elif point2 <= len(nums) - 2:
#                 point2 += 1
#         return [point1, point2]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

