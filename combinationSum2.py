class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack (start , curr , remaining) :
            if remaining == 0 :
                result.append(curr[:])
                return 
            if remaining < 0 :
                return 

            for index in range  ( start , len(candidates)):
                if index > start and candidates[index] == candidates[index - 1]:
                    continue

                curr.append (candidates[index])
                backtrack(index + 1, curr, remaining - candidates[index])
                curr.pop()
        backtrack (0 , [] , target)
        return result