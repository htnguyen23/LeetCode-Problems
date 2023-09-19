class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # iterate through list w/ L and R i ptr and find max difference
        max_prof = 0
        for l in range(len(prices)): 
            for r in range(l+1, len(prices)):
                max_prof = max(max_prof, prices[r] - prices[l])
                print(prices[r], '-', prices[l], '=', prices[r] - prices[l])
        return max_prof

# FASTER SOLUTION
class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         # use L and R i ptr to find max difference
#         # R ptr iterates through list to find mins and next mins in order
#         # keep track of max difference
#         profit, l, r, pbuy, psell = 0, 0, 1, 0, 0
#         while (r < len(prices)):
#             pbuy = prices[l]
#             psell = prices[r]
#             if (pbuy < psell):
#                 profit = max(profit, psell - pbuy)
#             else:
#                 l = r
#             r += 1
#         return profit
            
            
