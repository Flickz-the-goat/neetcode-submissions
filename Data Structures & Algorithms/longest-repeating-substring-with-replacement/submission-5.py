class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_l = 0
        saved_k = k
        prev = s[0]
        win = [prev]

        for c in s[1:]:
            if c != prev:
                k -= 1
                if k == -1:
                    l = len(win)
                    max_l = max(max_l, l+1)
                    k = saved_k
                    win = []
                prev = c
            win.append(c)
        return max(len(win), max_l)
