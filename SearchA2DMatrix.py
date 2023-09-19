class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]] 
        :type target: int
        :rtype: boo
        """
        
        low = 0 
        high = len(matrix[0]) * len(matrix) - 1
        i = 0
        while (low <= high):
            print("iteration " + str(i))
            mid = (low + high) // 2
            print("\tlow = " + str(low) + " high = " + str(high) + " mid = " + str(mid))
            val = matrix[mid // len(matrix[0])][mid%(len(matrix[0]))]
            print("\tvalue = " + str(val))
            print("\t\tmid//n = " + str(mid // len(matrix[0])) + ", mid%n = " + str(mid%(len(matrix[0]))) )
            if val == target:
                return True
            elif val < target:
                print("\t val < target")
                low = mid + 1
            else:
                print("\t val > target")
                high = mid - 1
            i += 1
        return False
    
    # idea: turn 2D bin search into 1D - divide by col? (how does modulo % give horizontal index)
    # [1, 3, 5, 7]
    # [10,11,16,20]
    # [23,30,34,60]]