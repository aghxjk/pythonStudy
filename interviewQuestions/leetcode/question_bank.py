"""
    给定一个整数数组nums 和 一个目标值target,请你在该数组中找出和为目标值的那个两个整数,
    并返回他们的数组下标。
"""


class Solution:
    @staticmethod
    def twoSum(nums, target):
        to_hash = dict(zip(nums, range(len(nums))))
        for i in range(len(nums)):
            other = target - nums[i]
            if to_hash.get(other):
                return [i, to_hash[other]]


result = Solution.twoSum([11, 2, 4, 7], 9)
print(result)
