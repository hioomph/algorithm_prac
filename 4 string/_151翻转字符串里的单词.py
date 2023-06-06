class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = list(s)
        # step1、在s后添加一个空格，方便后续遍历时的判断条件
        s.append(' ')
        n = len(s)

        # step2、创建一个空数组用于存放结构
        tmp = []
        count = 0
        for i in range(n):
            # step3、当遇到空格时，则将当前空格与上一个空格间非空的内容提取出来，作为一个整体的字符串append到tmp中
            if s[i] == ' ':
                # step4、去除内部存在的连续空格，减少为一个
                if i+1 < n and s[i+1] == ' ':
                    continue
                tmp.append(''.join(s[count:i]).strip())
                tmp.append(' ')
                count = i+1

        # step5、按照字符串反转的方式进行操作
        begin = 0
        end = len(tmp)-1
        while begin <= end:
            tmp_s = tmp[end]
            tmp[end] = tmp[begin]
            tmp[begin] = tmp_s
            begin += 1
            end -= 1

        return ''.join(tmp).strip()

    s = "a good   example"
    res = reverseWords(object, s=s)
    print(res)



