class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        m = n % (2*k)
        count = 1

        # 定义单次反转字符串操作
        def reverse(s, begin, end):
            while begin <= end:
                tmp = s[end]
                s[end] = s[begin]
                s[begin] = tmp
                begin += 1
                end -= 1
            return s

        for i in range(n):

            if (i+1) % (2*k) == 0:
                begin = 2*k*count - 2*k
                end = 2*k*count - k
                # reverse(s[begin, end], begin, end) list indices must be integers or slices, not tuple
                s = reverse(s, begin, end-1)
                count += 1
            elif i == n-m and k <= m < 2*k:
                begin = i
                end = i+k
                s = reverse(s, begin, end-1)
            elif i == n-m and m < k:
                begin = i
                end = n
                s = reverse(s, begin, end-1)
        return ''.join(s)

    s = "abcdefg"
    k = 8
    res = reverseStr(object, s=s, k=k)
    print(res)

