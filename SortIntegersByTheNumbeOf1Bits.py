class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ## better way:
        arr_list = list(arr)
        arr_list.sort(key=lambda x: (bin(x).count('1'), x))
        return arr_list

        # arr.sort(key=lambda x: (self.bin_1(x), x))
        # return arr


    # helper func to count number of 1's in the binary representation
    def bin_1(self, num):
        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count

        
