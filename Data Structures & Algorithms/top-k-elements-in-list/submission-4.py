class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n,0) + 1

        freq_buckets = [[] for i in range(len(nums)+1)]
        for n in counts.keys():
            freq_buckets[counts[n]].append(n)

        res = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        