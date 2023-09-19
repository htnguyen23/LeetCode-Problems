class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # use binary search b/c one half of the array is always sorted -> we only want to be looking in sorted side
        low = 0
        high = len(nums) - 1

        while low <= high:
            middle = (low + high) // 2
            # base case
            if nums[middle] == target:
                return middle
            
            # if left side is sorted 
            if nums[low] <= nums[middle]:
                # bin search on left side for target
                if (nums[low] <= target) and (target < nums[middle]): 
                    # target is in left side
                    high = middle - 1
                else:
                    # target is in right side -> right side can be sorted or unsorted
                    low = middle + 1
            # if left side is not sorted, then right side has to be sorted
            else:
                if (nums[middle] < target) and (target <= nums[high]):
                    # target is in right side
                    low = middle + 1
                else: 
                    # target is not in unsorted side
                    high = middle - 1

        return -1






