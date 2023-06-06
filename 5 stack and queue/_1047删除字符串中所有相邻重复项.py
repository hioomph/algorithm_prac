class Solution:
    def removeDuplicates(self, s: str) -> str:
        s = list(s)
        stack = []
        n = len(s)

        for i in range(n):
            # 若stack为空，则往里append元素
            if not stack:
                stack.append(s[i])
            # 若非空，则判断栈顶元素与要append的元素是否相等
            else:
                # 相等，则再次pop元素，去除重复项
                tmp = stack.pop()
                if tmp == s[i]:
                    continue
                # 不相等，则向栈中添加元素
                else:
                    stack.append(tmp)
                    stack.append(s[i])
        # for item in s:
        #     if stack and stack[-1] == item:
        #         stack.pop()
        #     else:
        #         stack.append(item)
        return ''.join(stack)

    s = 'abbaca'
    res = removeDuplicates(object, s=s)
    print(res)

