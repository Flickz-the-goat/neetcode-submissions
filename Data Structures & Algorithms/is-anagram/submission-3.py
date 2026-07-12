class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def gen_store(s: str):
            store = {}
            for c in s:
                if not store.get(c):
                    store[c] = 1
                else:
                    store[c] = store[c] + 1
            return store

        store_s = gen_store(s)
        store_t = gen_store(t)

        return store_s == store_t

