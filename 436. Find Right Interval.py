import bisect

class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        
        # Store tuple of (start_time, original_index)
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        
        # Extract only start times for fast binary search
        start_times = [s[0] for s in starts]
        
        ans = []
        for interval in intervals:
            end_val = interval[1]
            
            # Binary search to find smallest start >= end_val
            idx = bisect.bisect_left(start_times, end_val)
            
            if idx < n:
                ans.append(starts[idx][1])
            else:
                ans.append(-1)
                
        return ans
