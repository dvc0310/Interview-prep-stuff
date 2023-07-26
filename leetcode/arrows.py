class Solution(object):
    def findMinArrowShots(self, points):
        if len(points) == 0:
            return 0
        
        points.sort(key=lambda x: x[1])
        
        arrow_pos = points[0][1]
        
        count = 1
        
        for start, end in points:
            if start > arrow_pos:
                count += 1
                arrow_pos = end
                
        return count
    

    

points = [[1,2],[3,4],[5,6],[7,8]]
print(Solution().findMinArrowShots(points))
points = [[10,16],[2,8],[1,6],[7,12]]
print(Solution().findMinArrowShots(points))