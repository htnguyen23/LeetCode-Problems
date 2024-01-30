class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # ATTEMPT 3 - shorter code
        stepSum = 0
        minStep = float('inf')
        for num in nums:
            stepSum += num
            minStep = min(minStep, stepSum)
        if minStep < 1:
            return (-minStep + 1)
        return 1

        # # ATTEMPT 2
        # (1) iterate through num and add to start value when each step results in <= 1
        # start = 1
        # curr = 1
        # for num in nums:
        #     curr += num
        #     if curr < 1:
        #         start += -num
        #     if curr > 1:
        #         start -= num
        #     curr = 1
        # if start == 0:
        #     start += 1
        # return start

        # (2) use start value = 0, find lowest step sum, add complement so that lowest point will >= 1
        # start = 0
        # step_arr = []
        # min_step = float('inf')
        # for num in nums:
        #     start += num
        #     # i in arr corresponds to value of sum after ith iteration
        #     step_arr.append(start)
        #     min_step = min(min_step, start)

        # # print(nums)
        # # print(step_arr)

        # if min_step < 1:
        #     #print("lowest sum = " + str(min_step))
        #     start = -min_step + 1
        #     #print("start` = -(" + str(min_step) + ") + 1 = " + str(start))
        # elif min_step >= 1:
        #     #print("lowest sum = " + str(min_step) + ", is greater than 1")
        #     start = 1
        # else:
        #     start = 0

        # return start

        # # ATTEMPT 1 - implemented ending sum not being less than 1
        # # add up all step values to calculate what the difference should be for an end value >= 1
        # step_sum = sum(nums)
        # print("step_sum = " + str(step_sum))
        # start, = 0
        # # 1 <= step_sum + start
        # diff = 1 - step_sum
        # if diff >= 1:
        #     start = 1
        # elif diff <= 0:
        #     start = -diff
        # return start
            
