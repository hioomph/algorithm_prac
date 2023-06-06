from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 二维list排序
        people.sort(key=lambda x: (-x[0], x[1]))

        que = []
        # 根据每个元素的第二个维度k，贪心算法进行插入
        # people已经排序过了：同一高度时k值小的排前面
        for p in people:
            que.insert(p[1], p)

        return que



    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    res = reconstructQueue(object, people)
    print(res)
