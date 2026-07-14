class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums = sorted(nums)
        
        print(nums)

        for i, f in enumerate(nums):
            if f > 0:
                break
            
            j, k = i+1, len(nums)-1

            while j < k:
                s = nums[j] + nums[k] + f

                if s > 0: 
                    k -= 1
                elif s < 0:
                    j += 1
                else: 
                    if [f, nums[j], nums[k]] not in out:
                        out.append([f, nums[j], nums[k]])
                    j += 1
                    k -= 1

        return out