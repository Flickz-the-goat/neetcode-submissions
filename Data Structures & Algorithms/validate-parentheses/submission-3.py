class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s: 
            if c == "(" or c == "[" or c == "{":
                stack.insert(0, c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    o = stack[0]
                if o == "(" and c == ")":
                    stack.pop(0)
                elif o == "[" and c == "]":
                    stack.pop(0)
                elif o == "{" and c == "}":
                    stack.pop(0)
                else:
                    return False

        
        return len(stack) == 0