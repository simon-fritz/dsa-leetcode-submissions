class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        heap = []
        for key in counter:
            heapq.heappush(heap,(counter[key],key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq,num in heap]

        