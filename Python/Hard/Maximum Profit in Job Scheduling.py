from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        timestamp_map = {timestamp: index for index, timestamp in enumerate(sorted(set(startTime + endTime)))}
        
        jobs_by_start_time = {index: [] for index in range(len(timestamp_map))}
        for i in range(len(startTime)):
            start_index = timestamp_map[startTime[i]]
            end_index = timestamp_map[endTime[i]]
            jobs_by_start_time[start_index].append((start_index, end_index, profit[i]))

        max_profit = [0 for _ in range(len(timestamp_map))]

        for i in range(len(max_profit)):
            if i > 0:
                max_profit[i] = max(max_profit[i], max_profit[i-1])
            
            for start, end, p in jobs_by_start_time[i]:
                max_profit[end] = max(max_profit[end], max_profit[i] + p)
        
        return max(max_profit)
