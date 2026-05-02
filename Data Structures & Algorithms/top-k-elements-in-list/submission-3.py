class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n,0) + 1

        freq_buckets = [[] for i in range(len(nums)+1)]
        for n in counts.keys():
            freq_buckets[counts[n]].append(n)
        res = []
        for i in range(len(freq_buckets)-1,0,-1):
            if freq_buckets[i]:
                res += freq_buckets[i]
            if len(res) >= k:
                return res
        return res

        