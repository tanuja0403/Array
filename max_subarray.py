class Solution(object):
    def maxSubArray(self, nums):
        sum = 0 
        maxSum = float('-inf')
        for i in nums:
            sums += i 
            maxSum = max(maxSum , sums)
            if sums < 0 :
                sums = 0 
        return maxSums 