class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # ATTEMPT 2
        # use a DP 2D array to store intermediate results
        s_len = len(s)
        p_len = len(p)
        dp = [ [False] * (p_len + 1) for _ in range(s_len + 1) ]

        # edge case - an empty pattern matches an empty string
        dp[0][0] = True

        # fill the first row of the DP array
        for j in range(1, p_len + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
            
        # fill the dp array using buttom-up dynamic programming
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if (p[j - 1] == s[i - 1]) or (p[j - 1] == '?'):
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[s_len][p_len]

        # # ATTEMPT 1 
        # # iterate through string and sequence in parallel to match chars and ? * 
        # sptr, pptr = 0, 0
        # s_len = len(s)
        # p_len = len(p)
        # s_curr, p_curr = '',''
        # while sptr < s_len:
        #     s_curr, p_curr = s[sptr], p[pptr]
        #     # '*' matches any sequence of characters -> iterate until next criteria in p
        #     if p_curr == '*':
        #         # if there are no more criteria, rest of string is matching
        #         if pptr = p_len - 1:
        #             return True
        #         else:
        #             continue
        #     # '? ' matches any single character -> move on
        #     elif p_curr == '?':
        #         pptr += 1
        #         sptr += 1
        #     # char by char matching
