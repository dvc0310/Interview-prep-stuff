class Solution(object):
    def equalPairs(self, grid):
        mydict = {}
        for i in range(len(grid)):
            my_key = '|'.join(map(str, grid[i]))
            if my_key not in mydict:
                mydict[my_key] = 1
            else:
                mydict[my_key] += 1
        count = 0
        for col in range(len(grid[0])):
            list = []
            for row in range(len(grid)):
                list.append(grid[row][col])
            my_key = '|'.join(map(str, list))
            if my_key in mydict:
                count += mydict[my_key]
        
        return count



grid = [[11,1],[1,11]]
print(Solution().equalPairs(grid))