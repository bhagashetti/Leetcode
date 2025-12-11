class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        if n == 1:
            return False
        for char in s:
            if char=='(' or char == '[' or char == '{':
                stack.append(char)
            elif char==')' or char == ']' or char == '}':
                if len(stack) == 0:
                    return False
                else:
                    if char ==')':
                        c = stack.pop()
                        if c != "(":
                            return False
                    elif char == ']':
                        c = stack.pop()
                        if c != "[":
                            return False
                    elif char == '}':
                        c = stack.pop()
                        if c != "{":
                            return False
        if len(stack) != 0:
            return False
        else:
            return True


            