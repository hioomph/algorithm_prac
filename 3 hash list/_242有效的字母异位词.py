class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in s:
            record[ord(i) - ord('a')] += 1
        for i in t:
            record[ord(i) - ord('a')] -= 1
        # 经上述操作后，判断record中是否存在非0元素
        for i in range(26):
            if record[i] != 0:
                return False
        return True