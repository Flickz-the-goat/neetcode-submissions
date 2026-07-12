class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        while not i == len(nums):
            if not i == j:
                s = nums[i] + nums[j]
            
            if s == target:
                return [min(i, j), max(i, j)]
            if j == len(nums)-1:
                j = 0
                i += 1
            else: 
                j += 1