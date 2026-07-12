class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_arr = []

        for s in strs:
            encoded_arr.append(str(len(s)))
            encoded_arr.append("#")
            encoded_arr.append(s)
        
        return "".join(encoded_arr)

    def decode(self, s: str) -> List[str]:
        p = 0
        l_s = []
        while not p == len(s):
            l_arr = []
            while s[p] != "#":
                l_arr.append(s[p])
                p += 1
            l = int("".join(l_arr))
            p += 1
            temp = []
            for i in range(l):
                temp.append(s[p])
                p += 1
            l_s.append("".join(temp))

        return l_s
