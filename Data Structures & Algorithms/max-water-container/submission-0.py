class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_a = 0 
        while i < j: 
            w = j - i 
            h = min(heights[i], heights[j])

            a = w * h
            max_a = max(a, max_a)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
                
        return max_a
        