class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '[':
                stack.append(']')
            elif s[i] == '{':
                stack.append('}')
            else:
                if not stack:
                    return False
                elif s[i] != stack.pop():
                        return False
        if not stack:
            return True
        else:
            return False

    s = "]"
    res = isValid(object, s=s)
    print(res)