class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for s in strs: 
            ss = ''.join(sorted(s))
            if not out.get(ss):
                out[ss] = [s]
            else:
                out[ss].append(s)
        
        return list(out.values())
            

