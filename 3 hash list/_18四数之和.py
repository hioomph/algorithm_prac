# 双指针法
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []

        for j in range(n):
            if j > 0 and nums[j] == nums[j - 1]: continue  # 对nums[j]去重
            for i in range(j+1, n):
                left = i + 1
                right = n - 1
                # 因为target有正有负，因此再进行这个判断就错了
                # if nums[i] > target:
                # if nums[i] + nums[j] > target:
                #     break
                if i > j+1 and nums[i] == nums[i - 1]:  # 对nums[i]去重
                    continue
                while left < right:
                    total = nums[j] + nums[i] +nums[left] + nums[right]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        ans.append((nums[j], nums[i], nums[left], nums[right]))
                        while left != right and nums[left] == nums[left + 1]: left += 1
                        while left != right and nums[right] == nums[right - 1]: right -= 1
                        left += 1
                        right -= 1

        return ans

    nums = [1,-2,-5,-4,-3,3,3,5]
    res = fourSum(object, nums=nums, target=-11)
    print(res)
