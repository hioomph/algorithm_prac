class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(needle)
        b = len(haystack)
        if a == 0:
            return 0
        next = self.getNext(a=a, needle=needle)
        p = -1  # p为模式串起始位置
        for j in range(b):  # j为文本串起始位置
            while p >= 0 and needle[p+1] != haystack[j]:
                p = next[p]
            if needle[p+1] == haystack[j]:
                p += 1
            if p == a-1:  # p已经匹配到模式串的末尾
                return j-a+1  # 返回第一个匹配项的下标，j是当前文本串遍历到的索引，a为模式串长度
        return -1

    # 获取next数组
    def getNext(self, a, needle):
        next = ['' for i in range(a)]
        j = -1
        next[0] = j
        for i in range(1, len(needle)):  # j为-1时，i要从1开始
            while j > -1 and needle[j+1] != needle[i]:  # 前后缀不相同
                j = next[j]
            if needle[j+1] == needle[i]:  # 前后缀相同
                j += 1
            next[i] = j  # 记录i位置的最长前后缀长度为j
        return next
