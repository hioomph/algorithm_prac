from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        begin = 0
        end = len(s) - 1
        while begin <= end:
            tmp = s[end]
            s[end] = s[begin]
            s[begin] = tmp
            begin += 1
            end -= 1

    s = ["h","e","l","l","o"]
    reverseString(object, s)
    print(s)
