class MySolution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        hashmap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        start = 0
        st = ""
        _, lst = self.backtrack(digits, hashmap, start, st)
        return list(set(lst))


    def backtrack(self, digits, hashmap, index, st):
        lst = []
        s = ""
        if index >= len(digits):
            return st, lst
        
        for value in hashmap[digits[index]]:
            s, x = self.backtrack(digits, hashmap, index + 1, st + value)
            lst.extend(x)
            lst.append(s)
        
        return s, lst
    
class OptimalSolution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        hashmap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        result = []
        self.backtrack(digits, hashmap, 0, "", result)
        return result

    def backtrack(self, digits, hashmap, index, combination, result):
        if index == len(digits):
            result.append(combination)
            return
        for letter in hashmap[digits[index]]:
            self.backtrack(digits, hashmap, index + 1, combination + letter, result)



digits = "23"
my_solution = MySolution()
print(my_solution.letterCombinations(digits))

digits = "23"
optimal_solution = OptimalSolution()
print(optimal_solution.letterCombinations(digits))