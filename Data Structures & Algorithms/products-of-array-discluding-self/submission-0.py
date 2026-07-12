class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        for n in nums:
            cpy = nums.copy()
            cpy.pop(cpy.index(n))
            tp = 1
            for c in cpy:
                tp *= c
            out.append(tp)
        return out
