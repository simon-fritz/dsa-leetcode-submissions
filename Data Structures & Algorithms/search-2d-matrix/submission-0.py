class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)
        while l<r:
            m = (l+r)//2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] > target:
                r = m
            else:
                l = m+1
        row = r-1
        l = 0
        r = len(matrix[row])
        while l<r:
            m = (l+r)//2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m
            else:
                l = m+1
        return False
        
        