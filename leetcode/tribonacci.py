class Solution(object):
    def tribonacci_recursive(self, n):
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        return self.tribonacci_recursive(n - 1) + \
                self.tribonacci_recursive(n - 2) + \
                self.tribonacci_recursive(n - 3)


    def tribonacci(self, n):
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1

        T_n = 0
        T_n_plus_1 = 1
        T_n_plus_2 = 1
        current = 0
        
        for _ in range(3, n+1):
            current = T_n + T_n_plus_1 + T_n_plus_2
            T_n = T_n_plus_1
            T_n_plus_1 = T_n_plus_2
            T_n_plus_2 = current
        return current
