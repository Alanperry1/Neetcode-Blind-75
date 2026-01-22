# Time Complexity: O(n) - Single pass through the string
# Space Complexity: O(n) - Stack stores up to n/2 opening brackets
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        valid={
            ")":"(",
            "}":"{",
            "]":"["
        }

        for c in s:
            if c in valid:
                if stack and stack[-1]==valid[c]:
                    stack.pop()
                

            else:
                stack.append(c)
        return True if not stack else False

