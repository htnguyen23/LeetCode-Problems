class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # use L and R ptr to make sure both ends of string matches until the middle
        s = str(x)
        l, r, m = 0, len(s) - 1, 0
        # if len(s) % 2 == 1:
        #     m = r//2
        while (l < r):
            if (s[l] != s[r]):
                return False
            l += 1
            r -= 1
        return True

