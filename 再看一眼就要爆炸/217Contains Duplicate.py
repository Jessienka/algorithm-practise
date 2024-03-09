class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqSet = set(nums)
        return len(uniqSet) != len(nums)