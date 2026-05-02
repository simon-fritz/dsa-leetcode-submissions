class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index_stack = []
        res=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while index_stack and t > temperatures[index_stack[-1]]:
                cur_index = index_stack.pop()
                res[cur_index] = i - cur_index
            index_stack.append(i)
        return res


        