class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        for i in range(len(nums)-2):
            j,k = i+1, i+2
            while k != len(nums):
                s = nums[i] + nums[j] + nums[k]
                if s == 0 and [nums[i], nums[j], nums[k]] not in out and [nums[i], nums[k], nums[j]] not in out:
                    out.append([nums[i], nums[j], nums[k]])
                j += 1
                k += 1

        return out