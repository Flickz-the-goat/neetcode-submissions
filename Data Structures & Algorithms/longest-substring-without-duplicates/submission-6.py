class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        win = []
        max_len = 0

        for c in s:
            try:
                i = win.index(c)

                if len(win) > max_len:
                    max_len = len(win)
                win = win[i+1:]
                win.append(c)
                
            except ValueError:
                win.append(c)
        return max_len