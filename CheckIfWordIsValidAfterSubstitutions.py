class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # ATTEMPT 2 - use a stack to validate that each abc inserted in accounted for
        # iterate through s and add each char onto stack, once end of stack contains "abc", pop last 3 elems
        n = len(s)
        if (n < 3):
            return False
        stack = []
        i = 0

        while (i < n):
            stack.append(s[i])
            #print(stack)
            if (len(stack) >= 3):
                if (''.join(stack[-3:]) == 'abc'):
                    stack.pop(-1)
                    stack.pop(-1)
                    stack.pop(-1)
            i += 1
        
        if (len(stack) != 0):
            return False
        
        return True

        # # ATTEMPT 1 - checking logic doesn't fully cover edge cases
        # # iterate through s and compare to see if the out of sequence char is next to either 'a' or 'c' (left or right edge of inserted string)
        # # valid case 1: "abc" sequentially -> if a, right neighbor is b. if b, right neighor is c. if c, right neighor is a or null
        # # valid case 2: "abc" inserted -> if a, right neighbor is a or b. if b, right neighbor is a or c. if c, right neighbor is a or null
        # n = len(s)
        # if (n < 3):
        #     return False

        # aNum, bNum, cNum = 0, 0, 0
        # curr = s[0]
        # # first letter has to be 'a'
        # if (curr != 'a'):
        #     print(str(i) + "=" + s[i])
        #     return False

        # for i in range(n-1):
        #     curr = s[i]
        #     if (curr == 'a'):
        #         aNum += 1
        #         if (s[i+1] == 'c'):
        #             print(str(i) + "=" + s[i] + ", next is " + str(i+1) + "=" + s[i+1])
        #             return False
        #     elif (curr == 'b'):
        #         bNum += 1
        #         if (s[i+1] == 'b'):
        #             print(str(i) + "=" + s[i] + ", next is " + str(i+1) + "=" + s[i+1])
        #             return False
        #     elif (curr == 'c'):
        #         cNum += 1
        #         # if (s[i+1] != 'a'):
        #         #     return False
            
        # # handle last letter
        # curr = s[n-1]
        # if (curr == 'c'):
        #     cNum += 1
        #     # account for edge case of insertions that match the neighbor criteria by matching counts of all letters
        #     if (aNum == bNum) and (bNum == cNum):
        #     return True
        
        # print(str(aNum) + "=aNum , " + str(bNum) + "=bNum , " + str(cNum) + "=cNum")
        # return False