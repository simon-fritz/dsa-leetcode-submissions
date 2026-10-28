class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c)-ord("a")] += 1
            anagrams[str(counter)].append(s)
        return list(anagrams.values())