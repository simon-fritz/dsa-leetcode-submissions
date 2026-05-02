class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = {}
        for n in nums:
            s[n] = -1
        for i,n in enumerate(nums):
            if n+1 in s:
                s[n+1] = i
        max_counter = 0
        for key in s.keys():
            if s[key] != -1:
                continue
            counter = 1
            new_key = key + 1
            while new_key in s:
                counter += 1
                new_key = new_key + 1
            max_counter = max(counter, max_counter)
        return max_counter



        


        