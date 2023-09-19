class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

    # use queue to keep track of current bracket couples (ie. (), {}, [])
    # when a bracket is closed w/ correct type, couple is taken off queue
    # when close bracket is out of order, invalid string
                
        queue = [] # implement list as queue (append, pop)

        curr_c = ''
        for i in range(0, len(s)):
            curr_c = s[i]
            if (curr_c == '('):  # type1
                queue.append('(')
            if (curr_c == '{'):  # type2
                queue.append('{')
            if (curr_c == '['):  # type1
                queue.append('[')

            # take couple off queue when corresponding close bracket
            # if queue is empty, closing bracket does not have corresponding open bracket
            if len(queue) == 0:
                return False
            if (curr_c == ')'):
                if (queue[-1] == '('):  
                    queue.pop(-1)
                else:
                    return False  # if close bracket is not the bracket type, string is invalid
            if (curr_c == '}'):
                if (queue[-1] == '{'):  
                    queue.pop(-1)
                else:
                    return False
            if (curr_c == ']'):
                if (queue[-1] == '['):  
                    queue.pop(-1)
                else:
                    return False

        # if there's any brackets that haven't been closed, string is invalid
        if len(queue) > 0:
            return False
    
        return True
