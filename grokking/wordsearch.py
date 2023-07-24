class MySolution:
    def exist(self, board, word):
        hasWord = False
        for row in range(len(board)):
            for col in range(len(board) - 1):
                if word[0] == board[row][col]:
                    hasWord = self.dfs(board, row, col, word)
                    if hasWord:
                        return True
        return False

    def dfs(self, board, row, col, word):
        stack = [(row, col)]
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        wordIndex = 0
        while stack:
            y, x = stack.pop()
            if not visited[y][x] and board[y][x] == word[wordIndex]:
                visited[y][x] = True
                wordIndex += 1
                if wordIndex == len(word):
                    return True
                for newY, newX in self.neighbors(board, y, x):
                    if not visited[newY][newX]:
                        stack.append((newY, newX))

        return False

    def neighbors(self, board, row, col):
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        lst = []
        for direction in directions:
            newRow = row + direction[0]
            newCol = col + direction[1]
            if 0 <= newRow < len(board) and 0 <= newCol < len(board[0]):
                lst.append((newRow, newCol))
        return lst

class RecursiveSolution:
    def dfs(self, board, word, i, j, k):
        # check if current coordinates are out of grid or the current cell doesn't match the current character of the word
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
            return False
        # check if we have reached the end of the word
        if k == len(word) - 1:
            return True
        # mark the current cell as visited by replacing it with '/'
        tmp, board[i][j] = board[i][j], '/'
        # check all 4 adjacent cells recursively
        res = self.dfs(board, word, i+1, j, k+1) or \
                self.dfs(board, word, i-1, j, k+1) or \
                self.dfs(board, word, i, j+1, k+1) or \
                self.dfs(board, word, i, j-1, k+1)
        # backtrack by replacing the current cell with its original value
        board[i][j] = tmp
        return res

    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                # start the search from every cell
                if self.dfs(board, word, i, j, 0):
                    return True
        return False



def main():
  # Test Case 1
  board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
  ]
  word = "ABCCED"
  print(RecursiveSolution().exist(board, word)) # expected output: True

  # Test Case 2
  board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
  ]
  word = "SEE"
  print(MySolution().exist(board, word)) # expected output: True

  # Test Case 3
  board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
  ]
  word = "ABCB"
  print(MySolution().exist(board, word)) # expected output: False

  # Test Case 4
  board = [['a','a']]
  word = "aaa"
  print(MySolution().exist(board, word)) # expected output: False

  # Test Case 5
  board = [['a']]
  word = "a"
  print(MySolution().exist(board, word)) # expected output: True

  # Test Case 6
  board = [
      ['a','b','c','d','e'],
      ['f','g','h','i','j'],
      ['k','l','m','n','o'],
      ['p','q','r','s','t'],
      ['u','v','w','x','y'],
      ['z','a','b','c','d']
  ]
  word = "abcde"
  print(MySolution().exist(board, word)) # expected output: True

  # Test Case 7
  board = [
      ['a','b','c','d','e'],
      ['f','g','h','i','j'],
      ['k','l','m','n','o'],
      ['p','q','r','s','t'],
      ['u','v','w','x','y'],
      ['z','a','b','c','d']
  ]
  word = "zabcd"
  print(MySolution().exist(board, word)) # expected output: True

main()