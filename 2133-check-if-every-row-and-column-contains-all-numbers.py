class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        
        for i in range(n):
            rowSet = set()
            colSet = set()
            
            for j in range(n):
                rowSet.add(matrix[i][j])
                colSet.add(matrix[j][i])
            
            if len(rowSet) != n or len(colSet) != n:
                return False
            
        return True
