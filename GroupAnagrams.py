class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        word_dic = {}
        sorted_word = ""
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in word_dic:
                word_dic[sorted_word].append(word)
                #print(word_dic)
            else:
                word_dic[sorted_word] = [word]
        return word_dic.values()