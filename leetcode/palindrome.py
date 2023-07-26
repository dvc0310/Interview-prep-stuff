class Solution:
    def partition(self, s: str):
        palindrome_check_matrix = self.build_palindrome_check_matrix(s)
        return self.iterative_dfs(s, palindrome_check_matrix)

    def build_palindrome_check_matrix(self, s):
        palindrome_check_matrix = [[''] * len(s) for _ in range(len(s))]
        for end_idx in range(len(s)):
            for start_idx in range(end_idx + 1):
                if s[start_idx] == s[end_idx] and (end_idx - start_idx < 2 
                            or palindrome_check_matrix[start_idx + 1][end_idx - 1] != ''):
                    palindrome_check_matrix[start_idx][end_idx] = s[start_idx:end_idx+1]
        return palindrome_check_matrix

    def iterative_dfs(self, s, palindrome_check_matrix):
        stack = [(0, [])]
        results = []
        while stack:
            start_idx, partition = stack.pop()
            if start_idx == len(s):
                results.append(partition)
                continue
            for end_idx in range(start_idx, len(s)):
                if palindrome_check_matrix[start_idx][end_idx] != '':
                    stack.append((end_idx + 1, partition + [palindrome_check_matrix[start_idx][end_idx]]))
        return results


