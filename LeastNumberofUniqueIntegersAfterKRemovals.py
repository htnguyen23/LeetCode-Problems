class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # count occurence of elems into a dict, then remove k elements optimally so that there will be less unique elements (we want more that repeats)
        dic = {}
        for num in arr:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
        #print(dic)

        # # sort the dictionary based on values in increasing order - doesn't work?
        # sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1]))
        # print(sorted_dic)
        arr_list = dic.items()
        arr_list_sorted = sorted(arr_list, key=lambda x: x[1])

        count = 0
        total_elem = len(arr_list_sorted)
        del_elem = 0
        for num in arr_list_sorted:
            if k >= (count + num[1]):
                count += num[1]
                #print("\tcount = " + str(count) + " <= " + str(k))
                del_elem += 1
            else:
                #print("\tcount = " + str(count+num[1]) + " >= " + str(k))
                break
        #print(sorted_dic)
        return total_elem - del_elem
