class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack (index , curr , remaining):
            if remaining == 0 :
                result.append(curr[:])
                return result
            if remaining < 0 or index == len(candidates):
                return result
            
            #for single and multiple inclusion
            curr.append (candidates[index])
            backtrack (index , curr , remaining - candidates[index])
            curr.pop()

            #for no inclusion 
            backtrack (index + 1 , curr , remaining)

        backtrack ( 0 , [] , target )
        return result 



        
        