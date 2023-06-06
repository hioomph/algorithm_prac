from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5, count_10 = 0, 0
        for i in range(len(bills)):
            if bills[i] == 5:
                count_5 += 1
            elif bills[i] == 10:
                if count_5 > 0:
                    count_5 -= 1
                    count_10 += 1
                else:
                    return False
            elif bills[i] == 20:
                if count_10 > 0 and count_5 > 0:
                    count_5 -= 1
                    count_10 -= 1
                elif count_5 >= 3:
                    count_5 -= 3
                else:
                    return False

        return True
