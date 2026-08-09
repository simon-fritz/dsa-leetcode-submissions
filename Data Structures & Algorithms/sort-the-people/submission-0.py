class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        t = list(zip(names,heights))
        t.sort(key=lambda x: x[1], reverse=True)
        return [i[0] for i in t]
        