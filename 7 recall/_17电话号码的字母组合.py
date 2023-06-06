from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result: List[str] = []
        path = ''

        def backtracking(digits, index):
            nonlocal path
            if index == len(digits):
                result.append(path)
                return

            letters = letter_map[digits[index]]
            for letter in letters:
                path += letter
                backtracking(digits, index+1)
                path = path[:-1]

        if not digits:
            return []
        backtracking(digits, 0)
        return result

