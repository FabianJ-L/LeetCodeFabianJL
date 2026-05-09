class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        isOneTime = 0

        for i in nums:
            isOneTime ^= i

        return isOneTime
            
        