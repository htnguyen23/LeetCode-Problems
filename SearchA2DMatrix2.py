class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # use sorted row and col to traverse backwards & forwards (upper L corner is smallest, bottom R is biggest)
        m = len(matrix)     # row
        n = len(matrix[0])  # col
        # why can't start in middle? -> = (m-1) // 2, (n-1) // 2 
        row, col = 0, (n-1)     
        curr = 0

        # how to pick loop conditional? ()when does a num guarantee dec/inc?)
        while ( row < m and col < n and col >= 0 ):
            curr = matrix[row][col]
            if (curr == target):
                return True
            elif (curr > target):   
                # if curr is greater than target, then go backwards b/c the cols guarantee increase
                # if move leftwards, should not move rightwards again (eliminate R side)?
                col -= 1    # why not row -= 1? 
            else:
                # (curr < target)
                row += 1
        return False

        # [1,  4,  7,  11, 15]
        # [2,  5,  8,  12, 19]
        # [3,  6,  9,  16, 22]
        # [10, 13, 14, 17, 24]
        # [18, 21, 23, 26, 30]