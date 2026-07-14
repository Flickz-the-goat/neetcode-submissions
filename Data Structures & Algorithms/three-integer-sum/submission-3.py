class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums) - 1):
                for k in range(j+1, len(nums)):
                    s = nums[i] + nums[j] + nums[k]
                    if s == 0: 
                        alrdy_in = False
                        for o in out:
                            if nums[i] in o and nums[j] in o and nums[k] in o:
                                alrdy_in = True
                                break
                        if not alrdy_in:
                            out.append([nums[i], nums[j], nums[k]])

        return out