# ATTEMPT 3
class TimeMap(object):
    def __init__(self):
        self.dic = defaultdict(deque)

    def set(self, key, value, timestamp):
        self.dic[key].appendleft((timestamp, value))	#O(1) time complexity

    def get(self, key, timestamp):
        if self.dic[key]:
            for tv in self.dic[key]:	#O(N) time complexity, N = len(the key)
                if tv[0] <= timestamp:
                    return tv[1]
        return ''

# ATTEMPT 2 (changed decrement to iterating) - time limit exceeded 
# class TimeMap(object):

#     def __init__(self):
#         # data structure: a dict of dicts (each key has a value of a map with timestamps-value pairs) -> a hashmap
#         self.hashmap = {}


#     def set(self, key, value, timestamp):
#         """
#         :type key: str
#         :type value: str
#         :type timestamp: int
#         :rtype: None
#         """
#         if key not in self.hashmap:
#             self.hashmap[key] = {}
#         self.hashmap[key][timestamp] = value
#         #print(self.hashmap)
        

#     def get(self, key, timestamp):
#         """
#         :type key: str
#         :type timestamp: int
#         :rtype: str
#         """
#         # get dict from key
#         if key not in self.hashmap:
#             return "" 

#         currDict = self.hashmap[key]
#         #print(currDict)
#         # get value from timestamp, if timestamp doesn't exist, find the closest previous one
#         if timestamp in currDict:
#             return currDict[timestamp]
#         else:
#             timeskeys = currDict.keys()
#             timeskeys.sort()
#             #print(timeskeys)
#             for i in range(len(timeskeys)-1, -1, -1):
#                 if timeskeys[i] < timestamp:
#                     return currDict[timeskeys[i]]
#             return ""

        
# # ATTEMPT 1 - time limit exceeded
# # class TimeMap(object):

# #     def __init__(self):
# #         # data structure: a dict of dicts (each key has a value of a map with timestamps-value pairs) -> a hashmap
# #         self.hashmap = {}


# #     def set(self, key, value, timestamp):
# #         """
# #         :type key: str
# #         :type value: str
# #         :type timestamp: int
# #         :rtype: None
# #         """
# #         if key not in self.hashmap:
# #             self.hashmap[key] = {}
# #         self.hashmap[key][timestamp] = value
# #         #print(self.hashmap)
        

#     def get(self, key, timestamp):
#         """
#         :type key: str
#         :type timestamp: int
#         :rtype: str
#         """
#         # get dict from key
#         if key not in self.hashmap:
#             return ""
            
#         currDict = self.hashmap[key]
#         # get value from timestamp, if timestamp doesn't exist, decrease until it does
#         while (timestamp not in currDict) and (timestamp >= 1):
#             timestamp -= 1
#             # if finding prev timestamp by decrementing exceeds time limit, then have a sort dictionary
#         #print("timestamp=" + str(timestamp))
#         if timestamp:
#             #print("timestamp=" + str(timestamp) + " in key")
#             return currDict[timestamp]
#         else:
#             return ""

        
#         return 
        


# # Your TimeMap object will be instantiated and called as such:
# # obj = TimeMap()
# # obj.set(key,value,timestamp)
# # param_2 = obj.get(key,timestamp)