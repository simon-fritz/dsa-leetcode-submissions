class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        superSet = {}
        for i in range(9):
            superSet["col"+str(i)] = set()
            superSet["row"+str(i)] = set()
        for i in range(3):
            for j in range(3):
                superSet["square"+str(i)+"_"+str(j)] = set()
        for i in range(9):
            for j in range(9):
                square = str(i//3)+"_"+str(j//3)
                if board[i][j] == ".":
                    continue
                if board[i][j] in superSet["col"+str(j)] or \
                    board[i][j] in superSet["row"+str(i)] or \
                    board[i][j] in superSet["square"+square]:
                    return False
                superSet["col"+str(j)].add(board[i][j])
                superSet["row"+str(i)].add(board[i][j])
                superSet["square"+square].add(board[i][j])
        return True




        