''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 
''

class Solution:
    def checkStraightLine(self, coord: List[List[int]]) -> bool:
        try:
            slope=(coord[2][1]-coord[1][1])/(coord[2][0]-coord[1][0])

        except ZeroDivisionError:
            return False
            
        if(len(coord)==1):
            return True
        for i in range(len(coord)-1):
            try:
                slope1=(coord[i+1][1]-coord[i][1])/(coord[i+1][0]-coord[i][0])
            except ZeroDivisionError:
                return False
            if(slope==slope1):
                X=True
            else:
                return False
        
        return X

