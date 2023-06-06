class Solution:
    def isHappy(self, n: int) -> bool:

        record = {}

        # 1、获取n各位上的数字平方和
        def getSum(n):
            sum = 0
            while n != 0:
                sum += ((n % 10) ** 2)
                n = n // 10
            return sum

        # 2、将第一次得到的结果进行判断是否为1，否则会陷入死循环
        sum = getSum(n)
        if sum == 1:
            return True

        # 3、循环：1）更新record、sum；2）判断sum是否为record中已有的键，若是则返回False，若否则继续判断，注意1这个特殊情况
        else:
            record[sum] = 1
            while True:
                sum = getSum(sum)
                if sum in record.keys():
                    return False
                else:
                    record[sum] = 1
                if sum == 1:
                    return True

    res = isHappy(object, 3)
    print(res)

