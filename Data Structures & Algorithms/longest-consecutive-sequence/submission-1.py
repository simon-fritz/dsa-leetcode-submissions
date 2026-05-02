class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_counter = 0
        for n in s:
            if n-1 in s:
                continue
            counter = 1
            while n + counter in s:
                counter += 1
            max_counter = max(counter,max_counter)
        return max_counter





        


        