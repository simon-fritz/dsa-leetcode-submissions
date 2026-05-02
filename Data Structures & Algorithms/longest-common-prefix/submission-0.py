class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        for i in range(1,len(strs)):
            new_pref = ""
            for j in range(min(len(strs[i]),len(pref))):
                if pref[j] == strs[i][j]:
                    new_pref += pref[j]
                else:
                    break
            pref = new_pref    
        return pref