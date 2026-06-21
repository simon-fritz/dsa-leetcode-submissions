class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        maxkey,maxval = -1,-1
        for key in counter:
            if counter[key] > maxval:
                maxkey = key
                maxval = counter[key]
        return maxkey
