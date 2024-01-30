class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ATTEMPT 2 - Kadane's algorithm
        maxSum, currSum = nums[0], nums[0]

        for num in nums[1:]:
            currSum = max(num, currSum + num)
            maxSum = max(maxSum, currSum)

        return maxSum

        # # ATTEMPT 1
        # #iterate through arr w start and end ptr and make the optimal choice for larger sum based on including or excluding the ptrs
        # currSum = nums[0]
        # maxSum = float('-inf')
        # left, right = 0, 0
        # n = len(nums)

        # for i in range(1, n):
        #     # if inc. right gives higher sum, make the move
        #     right = i
        #     currSum += nums[i]

        #     # if inc. left gives higher sum, make the move
            
        
