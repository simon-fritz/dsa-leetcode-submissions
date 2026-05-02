class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = {}
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord("a")] += 1
            if str(chars) in sets:
                sets[str(chars)].append(s)
            else:
                sets[str(chars)] = [s]
        return list(sets.values())
