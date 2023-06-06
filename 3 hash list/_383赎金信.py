class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = {}

        for i in magazine:
            if i not in record.keys():
                record[i] = 1
            else:
                record[i] += 1

        for j in ransomNote:
            if j in record:
                record[j] -= 1
            if j not in record or record[j] < 0:
                return False
        return True

    res = canConstruct(object, 'aa', 'ab')
    print(res)