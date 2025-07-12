#435. Non-overlapping Intervals: https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        overlapping=0
        intervals = sorted(intervals,key=lambda x:x[1])
        # l = len(intervals)
        # start,end=0,1
        # while start<l and end<l:
        #     if intervals[start][1]>intervals[end][0]:
        #         overlapping += 1
        #         end += 1
        #     else:
        #         start = end
        #         end += 1
        # return overlapping

        k = -inf
        for x,y in intervals:
            if x>=k:
                k=y
            else:
               overlapping += 1
        return  overlapping