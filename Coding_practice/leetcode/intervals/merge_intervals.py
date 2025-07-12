class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key=lambda x:x[0])
        merged=[intervals[0]]
        n=len(intervals)
        for i in range(1,n):
            if merged[-1][1] >= intervals[i][0]:
                #merged[-1][0]=min(merged[-1][0],intervals[i][0])
                merged[-1][1]=max(merged[-1][1],intervals[i][1])
            else:
                merged.append(intervals[i])
        return merged