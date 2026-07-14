class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s: 
            if c == "(" or c == "[" or c == "{":
                stack.insert(0, c)
            else:
                stack.pop(0)
        
        return len(stack) == 0