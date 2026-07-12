class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(s: str, c: str):
            if len(s) != len(c):
                return False
            store_s = {}
            store_c = {}
            for i in range(len(s)):
                s_char = s[i]
                c_char = c[i]
                if not store_s.get(s_char):
                    store_s[s_char] =  1
                else:
                    store_s[s_char] = store_s.get(s_char) + 1
                
                if not store_c.get(c_char):
                    store_c[c_char] =  1
                else:
                    store_c[c_char] = store_c.get(c_char) + 1
            
            return store_s == store_c

        out = []
        while len(strs) != 0: 
            s = strs.pop(0)
            a = [s]
            for i in range(len(strs)):
                if is_anagram(s, strs[i]):
                    a.append(strs[i])
            out.append(a)

            for c in a:
                if c in strs:
                    strs.remove(c)
        return out
            

