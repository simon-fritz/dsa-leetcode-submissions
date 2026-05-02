class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}

        for l in s:
            s_count[l] = 1 + s_count.get(l,0)

        for l in t:
            t_count[l] = 1 + t_count.get(l,0)

        return s_count == t_count
        