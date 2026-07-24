class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 1
        win = {}

        for c in s:
            if win.get(c) is None:
                win[c] = 1
            else:
                l = len(win)
                win = {}
                if max_l < l:
                    max_l = l
        
        l = len(win)
        if max_l < l:
            max_l = l

        return max_l