class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        r = 0
        contains = set()
        for c in s:
            while l < r and s[r] in contains:
                contains.remove(s[l])
                l += 1
            contains.add(s[r])
            res = max(res,len(contains))
            r += 1
        return res