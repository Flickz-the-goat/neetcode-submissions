class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for n in nums:
            if not h.get(n):
                h[n] = 1
            else:
                h[n] += 1
        s = []
        for key in h:
            s.append([key, h[key]])
        ss = sorted(s, key= lambda x: x[1])

        out = []
        for i in range(k):
            out.append(ss.pop()[0])
        
        return out

        