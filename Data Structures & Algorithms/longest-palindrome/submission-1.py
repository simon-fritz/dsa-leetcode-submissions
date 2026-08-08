class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        print(counter)
        res = 0
        has_left = 0
        for key in counter:
            if counter[key] % 2 == 0:
                res += counter[key]
            else:
                res += counter[key]-1
                has_left = 1
        return res+has_left