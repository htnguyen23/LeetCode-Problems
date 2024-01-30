class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # greedy algorithm approach (prioritize the shortest intervals to minimize chance of overlap)  
        n = len(intervals)

        # sort intervals in ascending order based on endpoints
        intervals = sorted(intervals, key=lambda x: x[1])

        # iterate through intervals start & end time to find non-overlapping ones
        overlap = 0
        currEnd = intervals[0][1]
        for i in range(1, n):
            # interval starts when prev interval ends
            if intervals[i][0] < currEnd:
                overlap += 1
            else:
                currEnd = intervals[i][1]
        
        return overlap
                
