from typing import List


def count(punc, tmp1, tmp2):
    if punc == '+':
        return tmp2 + tmp1
    elif punc == '-':
        return tmp2 - tmp1
    elif punc == '*':
        return tmp2 * tmp1
    elif punc == '/':
        return tmp2 / tmp1


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack_num = []
        n = len(tokens)

        for i in range(n):
            if tokens[i].isdigit() or (tokens[i].split('-')[-1]).isdigit():
                stack_num.append(tokens[i])
            else:
                if len(stack_num) > 1:
                    tmp1, tmp2 = int(stack_num.pop()), int(stack_num.pop())
                    stack_num.append(count(tokens[i], tmp1, tmp2))

        return int(stack_num[-1])

    tokens = ["3","11","+","5","-"]
    res = evalRPN(object, tokens=tokens)
    print(res)