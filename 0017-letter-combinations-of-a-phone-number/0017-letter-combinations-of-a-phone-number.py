class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        t = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        @cache
        def dp(digits,word):
            final = []
            c = len(word)
            if c == len(digits):
                print(word)
                return [word]
            for letter in t[int(digits[c])]:
                final.extend(dp(digits,word+letter))
            
            return final
        
        return dp(digits,"")