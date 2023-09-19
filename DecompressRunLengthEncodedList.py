class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        decomp = []
        i, j = 0, 1
        #i_elem, j_elem = 0, 0 --> using elem outside of loop is less space complexity but more time complexity (why?)
        while (j <= len(nums)-1):
            for x in range(0, nums[i]):
                decomp.append(nums[j])
            i += 2
            j += 2
        return decomp
