class Solution :
    def twoSum (self , nums , target ):
        hash_map = {}
        for index,value in enumerate(nums):
            hash_map[index] = value

        for i in range (len(hash_map)):
            for j in range (i+1 , len(hash_map)):
                sum = hash_map[i] + hash_map[j]
                if sum == target :
                    return [i][j]