from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # 给胃口排序
        s.sort()  # 给饼干排序
        # 法1：先喂饱大胃口，先遍历胃口
        # start, count = len(s) - 1, 0
        # for i in range(len(g) - 1, -1, -1):
        #     if start >= 0 and g[i] <= s[start]:
        #         start -= 1
        #         count += 1
        # return count

        # 法2：先喂饱小胃口，先遍历饼干
        start, count = 0, 0
        for i in range(len(s)):
            if start < len(g) and g[start] <= s[i]:
                start += 1
                count += 1
        return count


