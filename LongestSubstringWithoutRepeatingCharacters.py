class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # keep track of chars seen and their last seen index
        seen_dict = {}
        # keep a L and R i ptr and iterate with R ptr
        l = 0
        curr = ''
        length = 0
        for r in range(len(s)):
            curr = s[r]
            if ( (curr in seen_dict) and (seen_dict[curr] >= l) ):
                l = seen_dict[curr] + 1
            else:
                length = max(length, r - l + 1)
            seen_dict[curr] = r
        return length
    
