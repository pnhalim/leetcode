class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []
        
        letters = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], 
                   '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r','s'],
                   '8': ['t','u','v'], '9': ['w','x','y','z']}

        dfs = []
        dfs.append(("", digits))
        ans = []

        while dfs:
            string, letter = dfs.pop()

            if letter == "":
                ans.append(string)
                continue

            curr, remaining = letter[0], letter[1:]
            add_this = [(string + c, remaining) for c in letters[curr]]
            print(add_this)
            for elem in add_this:
                dfs.append(elem)

        return ans