class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count occurences
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        freq_buckets = [[]for i in range(len(nums)+1)]
        for key in counter:
            freq_buckets[counter[key]].append(key)

        res = []
        for b in freq_buckets[::-1]:
            if b:
                res += b
                if len(res) == k:
                    break
        return res
        
            

        