class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if char == ')':
                    if len(stack) > 0:
                        p = stack.pop()
                        if p != '(':
                            return False
                    else:
                        return False
                elif char == ']':
                    if len(stack) > 0:
                        p = stack.pop()
                        if p != '[':
                            return False
                    else:
                        return False
                elif char == '}':
                    if len(stack) > 0:
                        p = stack.pop()
                        if p != '{':
                            return False
                    else:
                        return False
        if len(stack) > 0:
            return False
        return True