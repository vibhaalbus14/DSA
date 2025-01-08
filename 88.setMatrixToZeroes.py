#---------------------------approach with O(n+m) space-------------------
def matrix_change(matrix):
    noRows=len(matrix)
    noCols=len(matrix[0])

    rowList=[]
    colList=[]
    for i in range(noRows):
        for j in range(noCols):
            if matrix[i][j]==0:
                rowList.append(i)
                colList.append(j)
    print(rowList)
    print(colList)
    for i in rowList:
        matrix[i]=[0]*noCols
    for i in range(noRows):
        for j in colList:
            matrix[i][j]=0
    return matrix
print(matrix_change([[1,0,3],[4,5,6],[0,8,9]]))
#--------------------approach with const space-----------------------------------
def matrix_change(matrix):
    noRows=len(matrix)
    noCols=len(matrix[0])

    #use first row and col as marker
    
    ifFirstRowIsToBeMadeZero=0 #0=>No and 1=>Yes
    for i in range(noRows):
        for j in range(noCols):
            if matrix[i][j]==0:
                if i!=0: #is it first row?
                    matrix[0][j]=0 #marking the column that is to be made zero in first row
                    matrix[i][0]=0 #marking the row that is to be made zero in first coloumn
                else:
                    ifFirstRowIsToBeMadeZero=1
    #changing the rows
    for i in range(1,noRows):
        if matrix[i][0]==0:
            matrix[i]=[0]*noCols

    #changing the columns
    for j in range(noCols):
        if matrix[0][j]==0:
            for row in range(1,noRows):
                matrix[row][j]=0

    if ifFirstRowIsToBeMadeZero==1:
        matrix[0]=[0]*noCols

    return matrix
print(matrix_change([[1,0,3],[4,5,6],[0,8,9]]))

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        def makeColNone(col: int):
            # update the column to be None
            for r in range(len(matrix)):
                if matrix[r][col] != 0:
                    matrix[r][col] = None  # type: ignore
            pass

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    # make the column None
                    makeColNone(j)

                    # now update the row to be 0
                    for col in range(len(matrix[i])):
                        if matrix[i][col] != None and matrix[i][col] != 0:
                            matrix[i][col] = 0
                        elif matrix[i][col] == 0:
                            makeColNone(col)
                    break

        # now make all the None's 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == None:
                    matrix[i][j] = 0