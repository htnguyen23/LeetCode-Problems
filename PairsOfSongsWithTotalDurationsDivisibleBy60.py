class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        # # ATTEMPT 3 - similar to two sums problem 
        # we want to know for each t, how many x satisfy (t+x) % 60 = 0
        # edge case: t = 60 -> t % 60 = 0
        time_arr = [0] * 60
        rem = 0
        pairs = 0
        for t in time:
            # Calculate the remainder when the duration is divided by 60
            rem = t % 60
            # Check how many songs with complementary remainder we have seen so far
            pairs += time_arr[-rem] # account for edge case
            # Increment the count of current remainder
            time_arr[rem] += 1
        return pairs

        # # ATTEMPT 2 - wrong implementation, correct idea
        # # find combinations of pairs from number of occurences
        # # find sum in arr (use set), if divisible by 60, ...
        # time_dic = {}
        # max_t, min_t = 0, 0
        # pairs = 0

        # for t in time:
        #     if t not in time_dic:
        #         time_dic[t] = 0
        #     time_dic[t] += 1
        #     # if t == 60:
        #     #     time_dic[0] += 1      
        
        # rem = 0
        # for t in time_dic.keys():
        #     # if remainder is in dic, then num has a divisible pair
        #     rem = t % 60 
        #     if rem in time_dic:
        #         print("rem = " + str(rem) + ", divisible sum with: " + str(t) + ", pairs += " + str(time_dic[t] * time_dic[rem]))
        #         pairs += time_dic[t] * time_dic[rem]
        #     # if num remainder is 0, then num itself also adds pairs
        #     if rem == 0 and (time_dic[t] > 1):
        #         # combination formula = (n * (n-1)) / 2
        #         pairs += ((time_dic[t]) * (time_dic[t]-1)) / 2

        # print(time_dic)
        # return pairs

        # # ATTEMPT 1 - too long
        # # iterate through list and find pairs that are divisible by 60 (2 for loops = O(N^2))
        # n = len(time)
        # pairs = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if (time[i] + time[j]) % 60 == 0:
        #             pairs += 1
        
        # return pairs


        
