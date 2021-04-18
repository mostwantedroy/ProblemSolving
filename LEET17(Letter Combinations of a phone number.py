from copy import deepcopy

class Solution:
    def __init__(self):
        self.length = 0
        self.output = []
        self.hash_map = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        self.digits = ""

    def back_track(self, string, idx):

        if idx >= self.length:
            self.output.append(string)
            return
        
        for char in self.hash_map[self.digits[idx]]:
            string_new = deepcopy(string)
            string_new += char
            self.back_track(string_new, idx + 1)

    def letterCombinations(self, digits: str) -> List[str]:
        self.digits = digits
        self.length = len(digits)
        
        if self.length == 0:
            return self.output
        
        # digits = "259"

        self.back_track("", 0)
        
        return self.output