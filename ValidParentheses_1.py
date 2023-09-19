class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # flag for each type of bracket that opens
        # if another type's flag is raised when another flag is already raised, then is invalid string
        # if a close bracket is found while open flag is raised, then is invalid string
        valid = True
        type1_O = False  # type1 = ()
        type2_O = False  # type2 = {}
        type3_O = False  # type3 = []
        type1_C = False
        type_2_C = False
        type_3_C = False

        curr_char = ''
        # curr_type = ''    # to implement for validating strings of brackets with other chars within them - keep track of the current open bracket, for this problem, the current open bracket is the char 
        for i in range(0, len(s)):
            curr_char = s[i]
            # SET FLAGS
            if (curr_char == '('):
                type1_O = True
            if (curr_char == '{'):
                type2_O = True
            if (curr_char == '['):
                type3_O = True
            if (curr_char == ')'):
                type1_C = True
            if (curr_char == '}'):
                type2_C = True
            if (curr_char == ']'):
                type3_C = True
            
            # EVALUATE FLAGS
            # if there's a close flag without an open flag
            if ( ((not type1_O) and type1_C) or ((not type2_O) and type2_C) or ((not type3_O) and type3_C)):
                valid = False
                return valid
            # if there's a close bracket out of order (ie. '{ [ } ]' )
            if ( (curr_char == ')') ): # curr type is not type1
                return valid

