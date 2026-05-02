class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        string_set = set()
        max_len = 0
        while p2 < len(s):
            if s[p2] in string_set:
                string_set.remove(s[p1])
                p1 += 1
            else:
                string_set.add(s[p2])
                max_len = max(p2-p1+1 ,max_len)
                p2+=1
        return max_len