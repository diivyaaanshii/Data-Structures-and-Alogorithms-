class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows=len(matrix)
        col=len(matrix[0])
        top=0
        bot=rows-1

       
        while top<=bot:
            row=(top+bot)//2
            if target>matrix[row][-1]:
                top =row+1
            elif target < matrix[row][0]:
                bot=row-1
            else:
                break
        if not (top<=bot):
            return False
        row=(top+bot)//2
        left=0
        right=col-1
        while left<=right:
            mid=left+(right-left)//2
            if target > matrix[row][mid]:
                left=mid+1
            elif target<matrix[row][mid]:
                right=mid-1
            else:
                return True
        return False
