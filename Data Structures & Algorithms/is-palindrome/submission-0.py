class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        s = s.replace(" ", "")

        i, j = 0, len(s)-1

        while i < j:
            if not s[j].isalnum():
                j -= 1
                continue 
            elif not s[i].isalnum():
                i += 1
                continue 
            
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            else:
                return False
           
        return True