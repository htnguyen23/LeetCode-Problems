from collections import Counter

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # ATTEMPT 2 
        # Count the occurrences of each letter in the input string
        count = Counter(s)

        # Dictionary to store the counts of each digit
        digit_counts = {}

       # Identify unique letters for each digit and count their occurrences
        digit_counts['0'] = count['z']
        digit_counts['2'] = count['w']
        digit_counts['4'] = count['u']
        digit_counts['6'] = count['x']
        digit_counts['8'] = count['g']
        digit_counts['1'] = count['o'] - digit_counts['0'] - digit_counts['2'] - digit_counts['4']
        digit_counts['3'] = count['h'] - digit_counts['8']
        digit_counts['5'] = count['f'] - digit_counts['4']
        digit_counts['7'] = count['s'] - digit_counts['6']
        digit_counts['9'] = count['i'] - digit_counts['5'] - digit_counts['6'] - digit_counts['8']

        # Build the result string by repeating each digit based on its count
        result = ''.join(digit * digit_counts[digit] for digit in '0123456789')

        return result

        # # ATTEMPT 1
        # # determine number by first letter 
        # num_str = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
        # num_dic = {}
        # for i in range(10):
        #     num_dic[i] = 0
 
        # # iterate through str and count occurrences of each letter
        # s_dic = {}
        # for c in s:
        #     if c not in s_dic:
        #         s_dic[c] = 0
        #     s_dic[c] += 1
        
        # #count_dic = {}
        # count = float('inf')
        # for word in num_str.keys():
        #     count = float('inf')
        #     for letter in word:
        #         if letter in s_dic:
        #             count = min(count, s_dic[letter])
        #         else:
        #             count = 0
        #     #count_dic[word] = count
        #     num_dic[num_str[word]] = count
        
        # ret_str = ""
        # for num in num_dic.keys():
        #     ret_str += (str(num) * num_dic[num])

        # print(s_dic)
        # print(num_dic)
        # return ret_str
