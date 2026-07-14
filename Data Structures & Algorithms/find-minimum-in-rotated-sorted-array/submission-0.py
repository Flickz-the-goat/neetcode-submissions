class Solution:
    def findMin(self, nums: List[int]) -> int:

        low = 1001

        for n in nums: 
            if n < low:
                low = n

        return low
        