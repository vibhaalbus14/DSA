from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # def validate(num,row,col):
        #     #same row
        #     for c in range(n):
        #         if board[row][c]==num and c!=col:
        #             return False
        #     #same col
        #     for r in range(n):
        #         if board[r][col]==num and r!=row:
        #             return False
        #     #same sub square
        #     startRow=(row//3)*3
        #     startCol=(col//3)*3
        #     for i in range(startRow,startRow+3):
        #         for j in range(startCol,startCol+3):
        #             if board[i][j]==num and i!=row and j!=col:
        #                 return False
        #     return 
        
        column=defaultdict(set)
        row=defaultdict(set)
        subSquare=defaultdict(set)
        
        n=len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j]!=".":
                    num=board[i][j]
                    if num in row[i] or num in column[j] or num in subSquare[((i//3)*3,(j//3)*3)]:
                        return False
                    else:
                        column[j].add(num)
                        row[i].add(num)
                        subSquare[((i//3)*3,(j//3)*3)].add(num)

        return  True
        