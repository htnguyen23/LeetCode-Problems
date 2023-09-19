class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i1, i2, x, y = -1, -1, 0, 0
        flag = 0
        # iterate through list for an x finding a y in rest of list
        for num in nums:
            # x + y = target
            x = num 
            y = target - x
            if y in nums:
                i1 = nums.index(x)
                i2 = nums.index(y)
                if (i1 == i2):
                    print(nums[(i1+1):])
                    i2 = nums[(i1+1):].index(y)
        return [i1, i2]
        

# WORKING
        # for i in range(len(nums)):
        #     # x + y = target
        #     x = target - nums[i]
        #     if x in nums:
        #         i2 = nums.index(x)
        #         if (i2 == i):
        #             continue
        #             #print(nums[(i1+1):].index(3))
        #             #i2 = nums[(i1+1):].index(y)
        #         break
        # return [i, i2]

# BETTER SOLUTION
# find complement of elements
        # enumerate list to put into a dict for faster runtime from index search
        i_dict = {}
        complement = 0
        for i, num in enumerate(nums):
            complement = target - num
            if complement in i_dict:
                return [i_dict[complement], i]
            i_dict[num] = i
        return []
