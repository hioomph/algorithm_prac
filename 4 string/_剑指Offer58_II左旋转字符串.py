class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = list(s)

        s_left = s[:n]
        s_right = s[n:]

        return ''.join(s_right+s_left)