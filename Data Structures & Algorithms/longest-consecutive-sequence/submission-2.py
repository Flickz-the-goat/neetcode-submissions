class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = sorted(nums)
        max_count = 1
        count = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1] - 1:
                count += 1
            elif nums[i] == nums[i+1]:
                continue
            else: 
                if count > max_count:
                    max_count = count
                count = 1

        if count > max_count:
            max_count = count
          
        return max_count

