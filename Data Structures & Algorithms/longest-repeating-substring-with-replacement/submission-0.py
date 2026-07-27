class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        saved_k = k
        max_l = 0
        l = 1
        prev = s[0]
        for c in s[1:]:
            if prev == c:
                l += 1
            else:
                k -= 1
                l += 1
            
            if k == -1:
                max_l = max(max_l, l-1)
                k = saved_k
                l = 1
        return max(max_l, l)


