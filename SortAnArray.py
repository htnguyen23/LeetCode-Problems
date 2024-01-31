class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # O(nlog(n)) -> heap sort, merge sort

        # Merge sort (recursive) - divide & conquer approach where the array is broken down into individual parts to me sorted then merged back together until the entire array is sorted
        n = len(nums)
        # base case: arr is an individual elem (?)
        if (n <= 1):
            return nums

        # rec case: arr can be broken down more (n >= 2)
        arr1 = nums[:(n//2)]
        arr2 = nums[(n//2):]
        # sort the two halves to be able to merge them together (rec call)
        arr1 = self.sortArray(arr1)
        arr2 = self.sortArray(arr2)

        # merge two halves for completely sorted array (final rec call?)
        return self.mergeHelper(arr1, arr2)


    # helper function to be used in recursive merge sort function - takes two arrs and merges into one sorted array
    def mergeHelper(self, arr1, arr2):
        arrMerged = []
        i1, i2 = 0, 0
        n1, n2 = len(arr1), len(arr2)

        # populate the merged array by taking elems from arr1&2 one at a time
        while (i1 < n1) and (i2 < n2):
            # currElem in arr2 is next in sequential order
            if (arr1[i1] >= arr2[i2]):
                arrMerged.append(arr2[i2])
                i2 += 1
            else:
                arrMerged.append(arr1[i1])
                i1 += 1
            # print("i1 = " + str(i1) + ", i2 = " + str(i2))
            # print(arrMerged)
            
        # one of the arrs is now fully iterated through
        if (i1 != n1):
            arrMerged.extend(arr1[i1:])
        elif (i2 != n2):
            arrMerged.extend(arr2[i2:])
            
        return arrMerged