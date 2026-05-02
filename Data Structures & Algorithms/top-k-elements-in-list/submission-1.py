class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n,0) + 1
            
        tuples = list(counts.items())
        tuples.sort(reverse = True, key=lambda x: x[1])
        return [t[0] for t in tuples[:k]]
        