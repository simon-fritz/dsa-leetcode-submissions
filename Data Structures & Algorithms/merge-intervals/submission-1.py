class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0],x[1]),reverse=True)
        merged_intervals = []
        while intervals:
            cur = intervals.pop()
            if not merged_intervals:
                merged_intervals.append(cur)
                continue
            if cur[0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1],cur[1])
            else:
                merged_intervals.append(cur)
        return merged_intervals