class MySolution(object):
    def combinationSum3(self, k, n):
        hashmap = {
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
            6: False,
            7: False,
            8: False,
            9: False,
        }
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtrack(k, hashmap, 0, n, result, 1)
        return result

    def backtrack(self, k, hashmap, sum, n, result, num):
        if sum == n:
            return
    
        if sum > n or len(result) > k:
            sum -= result.pop()
            num = num + 1
            return
        
        if not hashmap[num]:
            result.append(num)
            sum += num
        
        self.backtrack(k, hashmap, sum, n, result, num + 1)
        
        return
    
class OptimalSolution:
    def combinationSum3(self, k, n):
        def dfs(remaining, path, start):
            # If the path has k numbers and their sum is n, append it to the result
            if remaining == 0 and len(path) == k:
                result.append(path)
                return
            # If path already has k numbers or remaining < 0, stop searching
            elif len(path) == k or remaining < 0:
                return
            # Continue to search
            for i in range(start, 10):
                dfs(remaining - i, path + [i], i + 1)

        result = []
        dfs(n, [], 1)
        return result


print(OptimalSolution().combinationSum3(3, 7))