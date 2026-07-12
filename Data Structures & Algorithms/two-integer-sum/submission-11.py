class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            k = nums[i]
            if(not d.get(k)):
                d[k] = [i]
            else:
                d[k].append(i)
        i = 0
        j = len(nums)-1
        c = sorted(nums)

        while not i == j:
            s = c[i] + c[j]
            if s == target:
                f = d.get(c[i]).pop(0)
                l = d.get(c[j]).pop(0)
                return [min(f, l), max(f,l)]
            elif s < target:
                i += 1 
            else:
                j -= 1
        
