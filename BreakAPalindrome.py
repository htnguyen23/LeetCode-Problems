class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        if (len(palindrome) <= 1):
            return ""

        # ATTEMPT 3: use palindromic quality to get next lexographically small letter - only need to look through first half of str
        lex_min = ord('a')
        lex_max = ord('z')
        icurr = 0
        not_palin = ""
        n = len(palindrome)
        for i in range(n//2):
            if ord(palindrome[i]) > lex_min:
                not_palin = palindrome[:i] + chr(lex_min) + palindrome[i+1:]
                return not_palin
        # first half of palindrome contains all 'a' -> change the last char to a b
        not_palin = palindrome[:n-1] + 'b'

        return not_palin

        # # ATTEMPT 2: only deal w first and second letter since that determines palindromic string - wrong, changing the second letter skips lexographic order from the rest of the chars
        # lex_min = ord('a')
        # lex_max = ord('z')
        # icurr = 0
        # not_palin = ""
        # if ord(palindrome[icurr]) > lex_min:
        #     not_palin = palindrome[:icurr] + chr(lex_min) + palindrome[icurr+1:]
        # else:
        #     # account for str of length 3 as changing the second letter won't affect the palindrome criteria
        #     if len(palindrome) == 3:
        #         icurr += 2
        #     else:
        #         icurr += 1
        #     if ord(palindrome[icurr]) > lex_min:
        #         not_palin = palindrome[:icurr] + chr(lex_min) + palindrome[icurr+1:]
        #     if ord(palindrome[icurr]) == lex_min:
        #         not_palin = palindrome[:icurr] + chr(lex_min+1) + palindrome[icurr+1:]

        # return not_palin

        # # ATTEMPT 1: iterate through str, and find the first place to put the smallest letter that isn't the current letter
        # icurr = 0 
        # not_palin = ""
        # found = 0
        # lex_min = ord('a')
        # lex_max = ord('z')
        # n = len(palindrome)
        # while(not found):
        #     print("icurr: " + str(icurr) + " = \"" + palindrome[:icurr+1] + "\"")
        #     if ord(palindrome[icurr]) > lex_min:
        #         print("\tcan replace " + palindrome[icurr] + " with " + chr(lex_min))
        #         found = 1
        #     icurr += 1
        #     if icurr == n:
        #         icurr = 0
        #         lex_min += 1
        #         print("lex_min = " + chr(lex_min))
        #         if lex_min > lex_max:
        #             return ""
        # not_palin = palindrome[:icurr] + chr(lex_min) + palindrome[icurr+1:]
        # return not_palin
