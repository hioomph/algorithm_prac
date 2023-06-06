from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if nums[i] > 0:
                break
            # nums[i] == nums[i - 1]，假设为a，而b+c是满足三数之和为0的固定值，因此若不去重，ans中会包含两个一样的元组(a,b,c)
            if i >= 1 and nums[i] == nums[i - 1]:  # 去重a
                continue
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    ans.append((nums[i], nums[left], nums[right]))
                    # 去重逻辑应该放在找到一个三元组之后，对b 和 c去重
                    while left != right and nums[left] == nums[left + 1]: left += 1
                    while left != right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
        return ans

    res = threeSum(object, [0, 0, 0, 0])
    print(res)

