class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # next lexographically larger -> start from rightmost (lexographically smaller would start from leftmost?)
        # sort array to find the lexographical order? -> if not constant extra memory
        # the first spot that has an increasing difference, find the next minimal increase in differnece

        # ATTEMPT 2
        # 1) find the first element to be swapped
        n = len(nums)
        i = n - 2
        while (i >= 0) and (nums[i] >= nums[i + 1]):
            i -= 1

        # 2) if no such pair is found, the array is in descending order
        if i == -1:
            nums.reverse() 

        # 3) find the smallest to the right of nums[i] that is greater than nums[i]
        else:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
        # 4) swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        # 5) reverse the elements to the right of nums[i]
            nums[i+1:] = reversed(nums[i+1:])

        # # ATTEMPT 1
        # n = len(nums)
        # i = n-2
        # while (i >= 0) and (nums[i] >= nums[i+1]):
        #     # find the first pair of consecutive elems where leftElem is less than rightElem
        #     # nums[i] is the first element to be swapped
        #     i -= 1
        
        # if i > -1:
        #     # find the smallest element to the right of nums[i] that is greater than nums[i]
        #     j = n-1
        #     while nums[j] < nums[i]:
        #         j -= 1
        #     # swap w/ the next smallest element
        #     swap = nums[i]
        #     nums[i] = nums[j]
        #     nums[j] = swap

        #     # reverse the elements to the right of nums[i]
        #     nums[i+1:] = reversed(nums[i+1:])

        # # decreasing diff -> does not have a lexicographically smaller arrangement
        # else:
        #     left, right = 0, n - 1
        #     while left < right:
        #         # Swap elements at left and right pointers
        #         nums[left], nums[right] = nums[right], nums[left]
        #         # Move pointers towards each other
        #         left += 1
        #         right -= 1
