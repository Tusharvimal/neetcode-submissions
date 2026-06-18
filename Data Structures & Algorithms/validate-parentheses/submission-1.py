class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] =='{' or s[i] == '[':
                stack.append(s[i])
                continue
            if len(stack) >= 1:
                if s[i] == ')' and stack[-1] != '(':
                    return False
                elif s[i] == '}' and stack[-1] != '{':
                    return False
                elif s[i] == ']' and stack[-1] != '[':
                    return False
                stack = stack[:-1]
            else:
                return False
        
        return len(stack) == 0
        