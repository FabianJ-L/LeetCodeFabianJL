class Solution(object):
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            for j, num1 in enumerate(nums):
                sum = num + num1
                if sum == target and i != j:
                    return i, j