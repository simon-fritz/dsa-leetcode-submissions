class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n,0) + 1
            
        keys = list(counts.keys())

        def counted(e):
            return counts[e]

        keys.sort(reverse = True, key=counted)

        return keys[0:k]
        